# Weather Data Pipeline

## Overview

This project demonstrates a complete ETL data pipeline using Python and BigQuery.

Pipeline Flow:

Open-Meteo API → Fetch → Transform → BigQuery

---

## API Chosen

Open-Meteo API

Reason:
- Free
- No authentication required
- Structured JSON response
- Good for transformation and analytics tasks

---

## Features

- API data fetching
- Error handling
- Logging
- Data transformation using pandas
- Derived analytical field
- BigQuery integration
- SQL analytics query

---

## Project Structure

task-2-data-pipeline/
│
├── src/
│ ├── fetch.py
│ ├── transform.py
│ ├── load_bigquery.py
│ └── main.py
│
├── sql/
│ └── weather_summary.sql
│
├── requirements.txt
└── README.md

---

## Derived Field

severity_score

Formula:

(humidity * wind_speed) / (temperature + 1)

This field helps identify potentially severe weather conditions.

---

## BigQuery Setup

Dataset:
weather_pipeline

Table:
weather_data

---

## Running the Pipeline

```bash
python src/main.py
```

---

## Example SQL Query

```sql
SELECT
    AVG(temperature) AS avg_temperature,
    AVG(humidity) AS avg_humidity,
    MAX(wind_speed) AS max_wind_speed,
    AVG(severity_score) AS avg_severity_score
FROM
    `notional-fusion-497517-s4.weather_pipeline.weather_data`;
```

---

## Production Considerations

### Scheduling

The pipeline could be scheduled using:
- Apache Airflow
- Cron jobs
- Google Cloud Scheduler

### Monitoring

Failure monitoring could include:
- Email alerts
- Cloud logging
- Retry mechanisms

### Scaling Improvements

For 10x larger data volume:
- Batch loading
- Partitioned BigQuery tables
- Parallel API requests
- Cloud-based orchestration

---

## Future Improvements

- Multiple city support
- Historical weather tracking
- Real-time dashboards
- Automated anomaly detection