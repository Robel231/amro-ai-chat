from flask import Blueprint, render_template, request, jsonify
from app import socketio
import openai
import os

# Define a Blueprint for the routes
main_routes = Blueprint('main', __name__)

# Set up the OpenAI API key
openai.api_key = "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"  # Make sure to use a secure method to store API keys

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
        # Call OpenAI API to generate a response using gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Update to gpt-3.5-turbo
            messages=[
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        ai_response = response.choices[0].message['content'].strip()

        # Format responses
        labeled_user_message = f"You: {user_message}"
        labeled_ai_response = f"Amro Response: {ai_response}"

        return jsonify({
            'user_message': labeled_user_message,
            'response': labeled_ai_response
        })
    except openai.error.OpenAIError as e:
        # Handle errors from the OpenAI API
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
        # Call OpenAI API to generate a response using gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Update to gpt-3.5-turbo
            messages=[
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        ai_response = response.choices[0].message['content'].strip()

        # Format responses
        labeled_user_message = f"You: {user_message}"
        labeled_ai_response = f"Amro Response: {ai_response}"

        # Emit the labeled response back to the client
        socketio.emit('response', {
            'user_message': labeled_user_message,
            'response': labeled_ai_response
        })
    except openai.error.OpenAIError as e:
        # Emit the error back to the client
        socketio.emit('response', {'error': str(e)})
