import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from src.data_preprocessing import preprocess_data

def train_model():
    X, y, scaler = preprocess_data("data/crop_data.csv")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, "model/crop_model.pkl")
    joblib.dump(scaler, "model/scaler.pkl")

    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_model()
