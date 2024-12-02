CREATE TABLE trade_logs (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20),
    trade_type VARCHAR(10), -- 'buy' or 'sell'
    entry_price DECIMAL(18, 8),
    exit_price DECIMAL(18, 8),
    stop_loss DECIMAL(18, 8),
    take_profit DECIMAL(18, 8),
    timestamp TIMESTAMP DEFAULT NOW(),
    profit_loss DECIMAL(18, 8)
);

CREATE TABLE bot_configurations (
    id SERIAL PRIMARY KEY,
    key VARCHAR(50),
    value TEXT
);

CREATE TABLE technical_indicators (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20),
    indicator_name VARCHAR(50),
    value DECIMAL(18, 8),
    timeframe VARCHAR(10),
    timestamp TIMESTAMP DEFAULT NOW()
);
