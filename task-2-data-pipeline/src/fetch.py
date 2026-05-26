import requests
import logging

logging.basicConfig(level=logging.INFO)

def fetch_weather_data():

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=13.08"
        "&longitude=80.27"
        "&hourly=temperature_2m,relative_humidity_2m,windspeed_10m"
    )

    try:
        logging.info("Fetching weather data from API...")

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        logging.info("Weather data fetched successfully")

        return data

    except requests.exceptions.RequestException as e:

        logging.error(f"API request failed: {e}")

        return None


if __name__ == "__main__":

    result = fetch_weather_data()

    print(result)