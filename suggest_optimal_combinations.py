import pandas as pd
from itertools import combinations

def load_data(filepath):
    return pd.read_csv(filepath)

def suggest_combinations(data, fertilizers, target_yield):
    possible_combinations = combinations(fertilizers, 2)
    optimal_combinations = []
    
    for combo in possible_combinations:
        subset = data[data['fertilizer_type'].isin(combo)]
        avg_yield = subset['crop_yield'].mean()
        if avg_yield >= target_yield:
            optimal_combinations.append((combo, avg_yield))
    
    return optimal_combinations

if __name__ == "__main__":
    filepath = "fertilizer_data.csv"  # Replace with your file
    target_yield = 500  # Replace with your target yield
    data = load_data(filepath)
    fertilizers = data['fertilizer_type'].unique()
    combinations = suggest_combinations(data, fertilizers, target_yield)
    print("Optimal Fertilizer Combinations for Target Yield:")
    for combo in combinations:
        print(combo)
