import pandas as pd
import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="fraud_db",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def load_transaction_data():
    conn = connect_to_db()
    if conn:
        query = """
        SELECT * FROM fraud_detection.transactions;
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    else:
        return None

if __name__ == "__main__":
    transactions = load_transaction_data()
    if transactions is not None:
        print("Transaction Data Loaded Successfully")
    else:
        print("Failed to load transaction data.")
