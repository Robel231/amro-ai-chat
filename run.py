from app import create_app, socketio

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    # Run the Flask app with SocketIO support
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
