import pandas as pd
import random

def generate_big_data(num_records=50000):
    print(f"Generating {num_records} mock employee performance records...")
    
    # Setup our organizational variables
    departments = ['Engineering', 'Product Tiger (Cross-Functional)', 'Marketing', 'Sales', 'Launchpad (Cross-Functional)']
    quarters = ['2026-Q1', '2026-Q2', '2026-Q3', '2026-Q4']
    
    # Synthesize data at scale
    data = {
        'emp_id': range(1, num_records + 1),
        'department': [random.choice(departments) for _ in range(num_records)],
        'quarter': [random.choice(quarters) for _ in range(num_records)],
        'projects_completed': [random.randint(1, 15) for _ in range(num_records)]
    }
    
    return pd.DataFrame(data)

def analyze_data_at_scale(df):
    print("\n--- Big Data Analytics Report ---")
    
    # Segment data by functional vs cross-functional teams
    df['is_cross_functional'] = df['department'].str.contains('Cross-Functional')
    
    # Run high-speed aggregations using Pandas
    summary = df.groupby('is_cross_functional')['projects_completed'].agg(['sum', 'mean', 'count'])
    summary.index = ['Functional Teams', 'Cross-Functional Teams']
    
    print(summary)
    print("--------------------------------")

if __name__ == "__main__":
    # 1. Generate the massive dataset
    large_dataset = generate_big_data(50000)
    
    # 2. Run the big data processing engine
    analyze_data_at_scale(large_dataset)