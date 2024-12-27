import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filepath):
    return pd.read_csv(filepath)

def generate_insights(data):
    sns.pairplot(data)
    plt.title("Feature Relationships")
    plt.show()
    
    correlation = data.corr()
    sns.heatmap(correlation, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

if __name__ == "__main__":
    filepath = "fertilizer_data.csv"  # Replace with your file
    data = load_data(filepath)
    generate_insights(data)
