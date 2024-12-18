from flask import Flask
from flask_socketio import SocketIO
from config import Config

# Initialize the SocketIO instance
socketio = SocketIO()

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    
    # Load configurations from config.py
    app.config.from_object(Config)
    
    # Initialize SocketIO with the app
    socketio.init_app(app)
    
    # Register routes
    from app.routes import app as main_routes
    app.register_blueprint(main_routes)
    
    return app
