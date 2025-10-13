from flask import Blueprint, render_template, request, jsonify
from app import socketio
from groq import Groq
import os

# Define a Blueprint for the routes
main_routes = Blueprint('main', __name__)

# Set up the Groq API key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@main_routes.route('/')
def index():
    """
    Render the main chat page.
    """
    return render_template('index.html')

@main_routes.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle the AI chat API endpoint.
    """
    # Extract the user message from the request
    user_message = request.json.get('message', '').strip()
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        # Call Groq API to generate a response
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            model="gemma-7b-it",
        )
        ai_response = chat_completion.choices[0].message.content.strip()


        # Format responses
        labeled_user_message = f"You: {user_message}"
        labeled_ai_response = f"Amro Response: {ai_response}"

        return jsonify({
            'user_message': labeled_user_message,
            'response': labeled_ai_response
        })
    except Exception as e:
        # Handle errors from the Groq API
        return jsonify({'error': str(e)}), 500

# Example SocketIO event handler
@socketio.on('message')
def handle_message(data):
    """
    Handle WebSocket messages.
    """
    user_message = data.get('message', '').strip()
    if not user_message:
        socketio.emit('response', {'error': 'No message provided'})
        return

    try:
        # Call Groq API to generate a response
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            model="gemma-7b-it",
        )
        ai_response = chat_completion.choices[0].message.content.strip()

        # Format responses
        labeled_user_message = f"You: {user_message}"
        labeled_ai_response = f"Amro Response: {ai_response}"

        # Emit the labeled response back to the client
        socketio.emit('response', {
            'user_message': labeled_user_message,
            'response': labeled_ai_response
        })
    except Exception as e:
        # Emit the error back to the client
        socketio.emit('response', {'error': str(e)})