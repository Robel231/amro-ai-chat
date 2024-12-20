from flask import Blueprint, render_template, request, jsonify
from app import socketio
import openai
import os

# Define a Blueprint for the routes
main_routes = Blueprint('main', __name__)

# Set up the OpenAI API key
openai.api_key = "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"

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
        # Call OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the model
            prompt=f"You: {user_message}\nAmro Response:",
            max_tokens=150,
            temperature=0.7
        )
        ai_response = response.choices[0].text.strip()

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
        # Call OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"You: {user_message}\nAmro Response:",
            max_tokens=150,
            temperature=0.7
        )
        ai_response = response.choices[0].text.strip()

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
