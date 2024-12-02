from db_connection import get_db_connection

def initialize_database():
    schema = """
    CREATE TABLE IF NOT EXISTS trade_logs (
        id SERIAL PRIMARY KEY,
        symbol VARCHAR(20),
        trade_type VARCHAR(10),
        entry_price DECIMAL(18, 8),
        exit_price DECIMAL(18, 8),
        stop_loss DECIMAL(18, 8),
        take_profit DECIMAL(18, 8),
        timestamp TIMESTAMP DEFAULT NOW(),
        profit_loss DECIMAL(18, 8)
    );

    CREATE TABLE IF NOT EXISTS bot_configurations (
        id SERIAL PRIMARY KEY,
        key VARCHAR(50),
        value TEXT
    );

    CREATE TABLE IF NOT EXISTS technical_indicators (
        id SERIAL PRIMARY KEY,
        symbol VARCHAR(20),
        indicator_name VARCHAR(50),
        value DECIMAL(18, 8),
        timeframe VARCHAR(10),
        timestamp TIMESTAMP DEFAULT NOW()
    );
    """
    connection = get_db_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute(schema)
                connection.commit()
                print("Database initialized successfully.")
        except Exception as e:
            print(f"Error initializing database: {e}")
        finally:
            connection.close()

if __name__ == "__main__":
    initialize_database()
