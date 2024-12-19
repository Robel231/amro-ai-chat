from gevent import monkey
monkey.patch_all()

from app import create_app, socketio

# Create the Flask app instance
app = create_app()

if __name__ == "__main__":
    socketio.run(app, debug=True)
