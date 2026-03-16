import pandas as pd
import numpy as np

def generate_hr_data():
    n = 1000
    np.random.seed(42)
    
    data = {
        'EmployeeID': [f"EMP-{1000+i}" for i in range(n)],
        'Age': np.random.randint(22, 60, n),
        'MonthlyIncome': np.random.randint(3000, 15000, n),
        'DistanceHome': np.random.randint(1, 50, n),
        'YearsAtCompany': np.random.randint(1, 15, n),
        'Overtime': np.random.choice([0, 1], n),
        'Department': np.random.choice(['Sales', 'R&D', 'HR'], n)
    }
    
    df = pd.DataFrame(data)
    
    # Logical Attrition: People with High Overtime and Low Income are 3x more likely to leave
    def determine_attrition(row):
        score = 0
        if row['Overtime'] == 1: score += 0.4
        if row['MonthlyIncome'] < 5000: score += 0.3
        if row['DistanceHome'] > 30: score += 0.2
        return 1 if (score + np.random.random() * 0.5) > 0.8 else 0

    df['Attrition'] = df.apply(determine_attrition, axis=1)
    df.to_csv('hr_data.csv', index=False)
    print("✅ Created hr_data.csv")

if __name__ == "__main__":
    generate_hr_data()