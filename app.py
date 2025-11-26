from fastapi import FastAPI
import joblib
import pandas as pd

# Φόρτωση μοντέλου
model = joblib.load("iris_model.pkl")

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "Iris Prediction API is running"}

@app.post("/predict")
def predict(features: dict):
    """
    Περιμένει JSON με τέσσερα χαρακτηριστικά, π.χ.:
    {
        "sepal length (cm)": 5.1,
        "sepal width (cm)": 3.5,
        "petal length (cm)": 1.4,
        "petal width (cm)": 0.2
    }
    """
    X = pd.DataFrame([features])
    prediction = model.predict(X)[0]
    return {"prediction": int(prediction)}

@app.get("/class_names")
def get_class_names():
    """
    Επιστρέφει τα ονόματα των κλάσεων και την αντιστοίχιση με τους αριθμούς.
    """
    return {
        "class_names": ["setosa", "versicolor", "virginica"],
        "mapping": {
            0: "setosa", 
            1: "versicolor", 
            2: "virginica"
        }
    }