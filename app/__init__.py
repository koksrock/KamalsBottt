from .config import Config
from dotenv import load_dotenv
import os

load_dotenv()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_SECRET_KEY = os.getenv("BYBIT_SECRET_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Create the Flask application
app = (__name__)

app.config.from_object(Config)
