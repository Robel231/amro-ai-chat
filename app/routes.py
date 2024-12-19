from flask import Blueprint, render_template, request, jsonify
from app import socketio

# Define a Blueprint for the routes
main_routes = Blueprint('main', __name__)

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
    
    # Mock response from ChatGPT (replace this with actual API call in production)
    response = f"ChatGPT Response to: {user_message}"
    
    return jsonify({'response': response})

# Example SocketIO event handler
@socketio.on('message')
def handle_message(data):
    """
    Handle WebSocket messages.
    """
    print(f"Message received: {data}")
    # Broadcast the message to all connected clients
    socketio.emit('response', {'message': f"Echo: {data}"})
