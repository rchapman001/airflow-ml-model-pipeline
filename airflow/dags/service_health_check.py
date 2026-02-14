from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from datetime import datetime

with DAG(
    dag_id="service_health_check",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["health", "debug"],
    is_paused_upon_creation=False,
) as dag:

    scraper_health = HttpOperator(
        task_id="scraper_health",
        http_conn_id="scraper_service",
        endpoint="/scraper-service/health",
        method="GET",
        log_response=True,
    )

    trainer_health = HttpOperator(
        task_id="trainer_health",
        http_conn_id="trainer_service",
        endpoint="/trainer-service/health",
        method="GET",
        log_response=True,
    )

    scraper_health >> trainer_health
