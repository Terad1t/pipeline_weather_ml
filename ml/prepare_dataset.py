import pandas as pd
from ml.db import get_engine


def load_dataset():

    engine = get_engine()

    query = """
        SELECT
            datetime,
            temperature,
            feels_like,
            temp_min,
            temp_max,
            pressure,
            humidity,
            wind_speed,
            wind_deg,
            clouds,
            visibility
        FROM sp_weather
        ORDER BY datetime
    """

    df = pd.read_sql(query, engine)

    # garantir datetime
    df["datetime"] = pd.to_datetime(df["datetime"])

    # features temporais
    df["hour"] = df["datetime"].dt.hour
    df["day_of_week"] = df["datetime"].dt.dayofweek
    df["month"] = df["datetime"].dt.month

    # target
    df["temp_tomorrow"] = df["temperature"].shift(-1)

    # lags
    df["temp_lag_1"] = df["temperature"].shift(1)
    df["temp_lag_2"] = df["temperature"].shift(2)
    df["temp_lag_3"] = df["temperature"].shift(3)

    df["temp_media_3"] = df["temperature"].rolling(3).mean()

    df = df.dropna()

    return df


if __name__ == "__main__":
    df = load_dataset()
    print(df.head())
    print(df.shape)