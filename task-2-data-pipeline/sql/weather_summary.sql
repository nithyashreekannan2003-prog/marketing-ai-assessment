SELECT
    AVG(temperature) AS avg_temperature,
    AVG(humidity) AS avg_humidity,
    MAX(wind_speed) AS max_wind_speed,
    AVG(severity_score) AS avg_severity_score
FROM
    `notional-fusion-497517-s4.weather_pipeline.weather_data`;