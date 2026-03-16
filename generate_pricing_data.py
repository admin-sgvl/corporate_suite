import pandas as pd
import numpy as np

def generate_pricing_data():
    # Simulate 50 different price tests
    prices = np.random.uniform(10, 50, 50)
    # Demand formula: Q = 1000 - 20*P + Noise
    quantities = 1000 - (18 * prices) + np.random.normal(0, 50, 50)
    
    df = pd.DataFrame({
        'Price': prices,
        'Quantity': [max(1, int(q)) for q in quantities]
    })
    
    df.to_csv('pricing_history.csv', index=False)
    print("✅ Created pricing_history.csv")

if __name__ == "__main__":
    generate_pricing_data()