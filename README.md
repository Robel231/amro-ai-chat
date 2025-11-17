# Amro AI Chat

## Description

Amro AI Chat is a real-time, web-based chatbot application powered by the Groq API. It provides a sleek, dark-themed interface for users to interact with an advanced AI model. The application is containerized using Docker for easy deployment and scalability.

## Features

- **Real-Time Chat:** Instantaneous messaging with the AI, powered by Flask-SocketIO.
- **AI-Powered Responses:** Intelligent and context-aware responses from the Groq API.
- **Modern Dark Theme:** A visually appealing and easy-on-the-eyes dark mode interface.
- **Responsive Design:** A clean and functional layout that adapts to various screen sizes.
- **PostgreSQL Database:** Stores chat history and other application data.
- **Containerized:** Dockerized for consistent development and production environments.

## Technical Stack

- **Backend:**
  - Python
  - Flask
  - Flask-SocketIO
  - Flask-SQLAlchemy
  - Gunicorn (for deployment)
  - Psycopg2 (for PostgreSQL connection)
- **Frontend:**
  - HTML
  - CSS
  - JavaScript
- **AI Integration:**
  - Groq API
  - `groq` Python library
  - `gemma-7b-it` model
- **Database:**
  - PostgreSQL
- **Deployment:**
  - Docker
  - Docker Compose

## Project Structure

```
/
├── wsgi.py               # WSGI entry point for Gunicorn
├── app/                  # Core application package
│   ├── __init__.py       # Application factory
│   ├── models.py         # SQLAlchemy models
│   └── routes.py         # API and web routes
├── config.py             # Configuration settings
├── templates/            # HTML templates
│   └── index.html
├── static/               # Static assets
│   ├── css/style.css
│   └── js/script.js
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker image definition
├── docker-compose.yml    # Docker Compose configuration
└── .env.txt              # Environment variables (e.g., API keys, DB credentials)
```

## Setup and Installation

To set up and run the project, you need Docker and Docker Compose installed.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd amro-ai-chat
    ```

2.  **Set up environment variables:**
    Create a `.env.txt` file in the root directory and add your Groq API key and database credentials:
    ```
    GROQ_API_KEY="your-groq-api-key"
    POSTGRES_DB=amro_db
    POSTGRES_USER=amro_user
    POSTGRES_PASSWORD=your_secure_postgres_password
    ```

3.  **Run the application with Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    The application will be available at `http://127.0.0.1:5000`.

## Usage

Simply open the application in your web browser, type a message in the input box, and press "Send" to start a conversation with Amro AI.

## License

This project is licensed under the MIT License.

## Contact

- **Name:** Robel Shemeles
- **Email:** Robelshemeles4@gmail.com
