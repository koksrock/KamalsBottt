import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DB_NAME = os.getenv("DB_NAME", "trading_db")
DB_USER = os.getenv("DB_USER", "trading_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "trading_password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_db_connection():
    try:
        connection = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            cursor_factory=DictCursor
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
