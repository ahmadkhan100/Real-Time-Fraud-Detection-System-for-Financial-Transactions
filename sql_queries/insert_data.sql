-- insert_data.sql

-- Insert sample data into customers table
INSERT INTO fraud_detection.customers (first_name, last_name, email) VALUES
('John', 'Doe', 'johndoe@example.com'),
('Jane', 'Smith', 'janesmith@example.com');

-- Insert sample data into transactions table
INSERT INTO fraud_detection.transactions (customer_id, transaction_amount, payment_method, transaction_status) VALUES
(1, 200.00, 'Credit Card', 'Completed'),
(1, 3000.00, 'Wire Transfer', 'Completed'),
(2, 150.00, 'PayPal', 'Completed'),
(2, 10000.00, 'Credit Card', 'Completed');
