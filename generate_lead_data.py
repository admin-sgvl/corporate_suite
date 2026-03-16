import pandas as pd
import numpy as np

def generate_lead_data():
    n = 1000
    data = {
        'LeadID': [f"L-{1000+i}" for i in range(n)],
        'WebVisits': np.random.randint(1, 25, n),
        'Source': np.random.choice(['Cold Call', 'LinkedIn', 'Referral', 'Webinar'], n),
        'TimeSpentMin': np.random.randint(1, 60, n),
        'TotalEmails': np.random.randint(0, 10, n)
    }
    
    df = pd.DataFrame(data)
    
    # Logic: Referrals + high web visits = high conversion
    def calc_conv(row):
        score = 0
        if row['Source'] == 'Referral': score += 0.5
        if row['WebVisits'] > 15: score += 0.3
        if row['TimeSpentMin'] > 30: score += 0.2
        return 1 if (score + np.random.random() * 0.4) > 0.8 else 0

    df['Converted'] = df.apply(calc_conv, axis=1)
    df.to_csv('lead_data.csv', index=False)
    print("✅ Created lead_data.csv")

if __name__ == "__main__":
    generate_lead_data()