import os
from gevent import monkey
monkey.patch_all()  # Ensure compatibility with async features

from app import create_app, socketio

# Create the Flask app instance
app = create_app()

# Debugging to verify if the templates directory and index.html exist
template_path = os.path.join(os.getcwd(), 'templates', 'index.html')
if not os.path.exists(template_path):
    print(f"Error: Template not found at {template_path}")
else:
    print(f"Template found: {template_path}")

# Entry point for running the application
if __name__ == "__main__":
    # Use socketio to run the app with debugging enabled for development
    socketio.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
