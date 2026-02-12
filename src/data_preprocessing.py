import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(csv_path):
    df = pd.read_csv(csv_path)

    X = df.drop("label", axis=1)
    y = df["label"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler
