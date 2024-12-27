import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    return pd.read_csv(filepath)

def monitor_health(data):
    health_metrics = ['nutrient_level', 'disease_index', 'water_content']
    for metric in health_metrics:
        if metric in data.columns:
            plt.plot(data['timestamp'], data[metric], label=metric)
    
    plt.xlabel("Time")
    plt.ylabel("Metric Value")
    plt.title("Crop Health Monitoring")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    filepath = "crop_health_data.csv"  # Replace with your file
    data = load_data(filepath)
    monitor_health(data)
