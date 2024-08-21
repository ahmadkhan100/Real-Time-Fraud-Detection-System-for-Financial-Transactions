-- fraud_detection_queries.sql

-- Query to find potentially fraudulent transactions based on simple rules
-- Example: Flag transactions above a certain amount as potentially fraudulent
SELECT
    transaction_id,
    customer_id,
    transaction_amount,
    transaction_date,
    payment_method,
    transaction_status
FROM
    fraud_detection.transactions
WHERE
    transaction_amount > 5000 -- Adjust threshold as necessary
    OR payment_method = 'Wire Transfer' -- Example condition for high-risk methods
    OR transaction_status = 'Failed';
