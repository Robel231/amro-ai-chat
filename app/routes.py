from flask import Blueprint, render_template, request, jsonify
from app import socketio
import openai
import os

# Define a Blueprint for the routes
main_routes = Blueprint('main', __name__)

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        # Call OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the model
            prompt=user_message,
            max_tokens=100,
            temperature=0.7
        )
        ai_response = response.choices[0].text.strip()
        return jsonify({'response': ai_response})
    except openai.error.OpenAIError as e:
        # Handle errors from the OpenAI API
        return jsonify({'error': str(e)}), 500

# Example SocketIO event handler
@socketio.on('message')
def handle_message(data):
    """
    Handle WebSocket messages.
    """
    user_message = data.get('message', '')
    if not user_message:
        socketio.emit('response', {'error': 'No message provided'})
        return
    
    try:
        # Call OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=100,
            temperature=0.7
        )
        ai_response = response.choices[0].text.strip()
        # Emit the response back to the client
        socketio.emit('response', {'message': ai_response})
    except openai.error.OpenAIError as e:
        # Emit the error back to the client
        socketio.emit('response', {'error': str(e)})
