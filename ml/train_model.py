import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

from ml.prepare_dataset import load_dataset


def train():

    df = load_dataset()

    if len(df) < 5:
        raise ValueError("Dataset muito pequeno para treinar modelo")

    X = df.drop(columns=["datetime", "temp_tomorrow"])
    y = df["temp_tomorrow"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False)

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42)

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    print("MAE:", mae)
    joblib.dump(model, "model.pkl")
    print("Modelo salvo em model.pkl")


if __name__ == "__main__":
    train()