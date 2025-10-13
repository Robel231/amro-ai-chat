import os
from gevent import monkey
monkey.patch_all()

from app import create_app, socketio

# Create the Flask app instance
app = create_app()  # Renamed back to `app` to align with Gunicorn expectations

# Debug to check if templates directory exists and index.html is in place
template_path = os.path.join(os.getcwd(), 'templates', 'index.html')
if not os.path.exists(template_path):
    print(f"Error: Template not found at {template_path}")
else:
    print(f"Template found: {template_path}")

# Run the app (used for local development)
if __name__ == "__main__":
    socketio.run(app, debug=True)
