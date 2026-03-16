import pandas as pd
import random

def generate_baskets():
    items = ['Bread', 'Milk', 'Eggs', 'Beer', 'Diapers', 'Coffee', 'Sugar', 'Butter', 'Cereal']
    data = []
    
    for i in range(1, 501): # 500 Transactions
        invoice_id = f"INV-{i}"
        
        # Random items
        basket_size = random.randint(1, 4)
        selected_items = random.sample(items, basket_size)
        
        # Add a specific pattern: 70% of people who buy Beer also buy Diapers
        if 'Beer' in selected_items and random.random() < 0.7:
            if 'Diapers' not in selected_items:
                selected_items.append('Diapers')
                
        for item in selected_items:
            data.append([invoice_id, item])
            
    df = pd.DataFrame(data, columns=['InvoiceID', 'ItemName'])
    df.to_csv('market_basket_data.csv', index=False)
    print("✅ Created market_basket_data.csv")

if __name__ == "__main__":
    generate_baskets()