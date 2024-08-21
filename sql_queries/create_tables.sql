-- create_tables.sql

CREATE SCHEMA fraud_detection;

CREATE TABLE fraud_detection.transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INT,
    transaction_amount DECIMAL(10, 2),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    transaction_status VARCHAR(50)
);

CREATE TABLE fraud_detection.customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE fraud_detection.fraud_logs (
    log_id SERIAL PRIMARY KEY,
    transaction_id INT REFERENCES fraud_detection.transactions(transaction_id),
    detection_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fraud_detected BOOLEAN,
    fraud_reason TEXT
);
