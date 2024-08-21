import pandas as pd
import numpy as np

def detect_fraud(transactions_df):
    # Simple rule-based fraud detection example
    fraud_flags = []

    for _, transaction in transactions_df.iterrows():
        if transaction['transaction_amount'] > 5000:
            fraud_flags.append((transaction['transaction_id'], True, "High transaction amount"))
        elif transaction['payment_method'] == 'Wire Transfer':
            fraud_flags.append((transaction['transaction_id'], True, "High-risk payment method"))
        elif transaction['transaction_status'] == 'Failed':
            fraud_flags.append((transaction['transaction_id'], True, "Transaction failed"))
        else:
            fraud_flags.append((transaction['transaction_id'], False, "No issues detected"))

    return pd.DataFrame(fraud_flags, columns=['transaction_id', 'fraud_detected', 'fraud_reason'])

if __name__ == "__main__":
    from data_processing import load_transaction_data

    transactions_df = load_transaction_data()
    if transactions_df is not None:
        fraud_results = detect_fraud(transactions_df)
        print(fraud_results)
    else:
        print("No transaction data available for fraud detection.")
