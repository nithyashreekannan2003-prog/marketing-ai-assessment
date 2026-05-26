from fetch import fetch_weather_data
from transform import transform_weather_data
from load_bigquery import load_to_bigquery

def main():

    raw_data = fetch_weather_data()

    transformed_df = transform_weather_data(raw_data)

    if transformed_df is not None:

        load_to_bigquery(transformed_df)

        print(transformed_df.head())

if __name__ == "__main__":

    main()