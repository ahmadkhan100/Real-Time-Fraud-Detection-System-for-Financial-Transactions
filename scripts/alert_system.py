import smtplib
from email.mime.text import MIMEText
import pandas as pd

def send_alert(recipient, subject, body):
    sender = "your_email@example.com"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender, "your_password")
            server.sendmail(sender, [recipient], msg.as_string())
            print(f"Alert sent to {recipient}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

def alert_for_fraud(fraud_results_df):
    for _, row in fraud_results_df.iterrows():
        if row['fraud_detected']:
            message = f"Fraudulent transaction detected!\nTransaction ID: {row['transaction_id']}\nReason: {row['fraud_reason']}"
            send_alert("recipient@example.com", "Fraud Alert", message)

if __name__ == "__main__":
    from fraud_detection import detect_fraud
    from data_processing import load_transaction_data

    transactions_df = load_transaction_data()
    if transactions_df is not None:
        fraud_results = detect_fraud(transactions_df)
        alert_for_fraud(fraud_results)
    else:
        print("No transaction data available for fraud detection.")
