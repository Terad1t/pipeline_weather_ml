import joblib
from ml.prepare_dataset import load_dataset


def predict():

    df = load_dataset()

    model = joblib.load("model.pkl")

    X = df.drop(columns=["datetime", "temp_tomorrow"])

    last_row = X.iloc[-1:]

    prediction = model.predict(last_row)[0]

    return float(prediction)


if __name__ == "__main__":
    print(predict())