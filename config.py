import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    # Flask secret key for session management and CSRF protection
    SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")
    
    # OpenAI API key for integration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Enable or disable Flask's debugging mode
    DEBUG = os.getenv("DEBUG", "True") == "True"
