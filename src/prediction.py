import joblib
import numpy as np

model = joblib.load("model/crop_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def predict_crop(N, P, K, temp, humidity, ph):
    input_data = np.array([[N, P, K, temp, humidity, ph]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    return prediction[0]
