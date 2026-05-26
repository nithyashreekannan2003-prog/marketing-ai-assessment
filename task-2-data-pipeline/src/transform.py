import pandas as pd
import logging
from fetch import fetch_weather_data

logging.basicConfig(level=logging.INFO)

def transform_weather_data(data):

    try:

        hourly = data["hourly"]

        df = pd.DataFrame({
            "timestamp": hourly["time"],
            "temperature": hourly["temperature_2m"],
            "humidity": hourly["relative_humidity_2m"],
            "wind_speed": hourly["windspeed_10m"]
        })

        # Derived analytical field
        df["severity_score"] = (
            df["humidity"] * df["wind_speed"]
        ) / (df["temperature"] + 1)

        logging.info("Transformation completed successfully")

        return df

    except Exception as e:

        logging.error(f"Transformation failed: {e}")

        return None


if __name__ == "__main__":

    raw_data = fetch_weather_data()

    transformed_df = transform_weather_data(raw_data)

    print(transformed_df.head())