from google.cloud import bigquery
import logging

logging.basicConfig(level=logging.INFO)

def load_to_bigquery(df):

    try:

        client = bigquery.Client()

        table_id = "notional-fusion-497517-s4.weather_pipeline.weather_data"

        job = client.load_table_from_dataframe(df, table_id)

        job.result()

        logging.info("Data loaded successfully into BigQuery")

    except Exception as e:

        logging.error(f"BigQuery load failed: {e}")