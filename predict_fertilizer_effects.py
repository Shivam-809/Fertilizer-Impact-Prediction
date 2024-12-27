import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(data):
    data = data.dropna()
    categorical_cols = data.select_dtypes(include=['object']).columns
    data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)
    return data

def train_model(X_train, y_train):
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model

def forecast_effects(filepath, target_column):
    data = load_data(filepath)
    data = preprocess_data(data)
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f"Forecasting Performance - MSE: {mse}, R2: {r2}")
    return model

if __name__ == "__main__":
    filepath = "fertilizer_data.csv"  # Replace with your file
    target_column = "crop_yield"
    forecast_effects(filepath, target_column)
