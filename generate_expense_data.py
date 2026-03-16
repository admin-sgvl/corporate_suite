import pandas as pd
import numpy as np

def generate_expense_data():
    n = 1000
    # Normal Transactions
    data = {
        'TransactionID': [f"TXN-{2000+i}" for i in range(n)],
        'Amount': np.random.normal(200, 50, n), # Most expenses around $200
        'VendorRating': np.random.uniform(3, 5, n),
        'Category': np.random.choice(['Office Supplies', 'Travel', 'Software', 'Meals'], n)
    }
    
    df = pd.DataFrame(data)
    
    # Inject 5 Anomaly "Frauds"
    fraud_data = pd.DataFrame({
        'TransactionID': [f"FLAG-{i}" for i in range(5)],
        'Amount': [5000, 7500, 12000, 4500, 8000], # Way too high
        'VendorRating': [1.2, 0.5, 1.0, 2.1, 0.8], # Poorly rated vendors
        'Category': ['Office Supplies', 'Software', 'Travel', 'Meals', 'Office Supplies']
    })
    
    df = pd.concat([df, fraud_data], ignore_index=True)
    df.to_csv('expense_data.csv', index=False)
    print("✅ Created expense_data.csv with injected anomalies.")

if __name__ == "__main__":
    generate_expense_data()