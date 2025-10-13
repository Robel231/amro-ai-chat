from flask import Flask
from flask_socketio import SocketIO
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Initialize the SocketIO instance with gevent as the async mode
socketio = SocketIO(async_mode="gevent")
db = SQLAlchemy()

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    
    # Load configurations from config.py
    app.config.from_object(Config)

    # Initialize extensions
    socketio.init_app(app)
    db.init_app(app)
    
    # Import and register routes
    from app.routes import main_routes
    app.register_blueprint(main_routes)
    
    return app
