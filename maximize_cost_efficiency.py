import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def calculate_efficiency(data):
    data['efficiency'] = data['crop_yield'] / data['fertilizer_cost']
    return data.sort_values(by='efficiency', ascending=False)

if __name__ == "__main__":
    filepath = "fertilizer_data.csv"  # Replace with your file
    data = load_data(filepath)
    efficiency_data = calculate_efficiency(data)
    print("Top Fertilizers by Efficiency:")
    print(efficiency_data[['fertilizer_type', 'efficiency']].head(10))
