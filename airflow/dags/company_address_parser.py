from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from airflow.models.param import Param
from datetime import datetime

with DAG(
    dag_id="company_address_parser",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["scraper", "company"],
    is_paused_upon_creation=False,
    params={
        "size": Param("small", enum=["small", "medium", "large"]),
    },
) as dag:

    scrape_company = HttpOperator(
        task_id="scrape_company_addresses",
        http_conn_id="scraper_service",
        endpoint="/scraper-service/company-address?size={{ params.size }}",
        method="GET",
        log_response=True,
    )

    train_model = HttpOperator(
        task_id="train_address_parser",
        http_conn_id="trainer_service",
        endpoint="/trainer-service/train-address-model?size={{ params.size }}",
        method="GET",
        log_response=True,
    )

    scrape_company >> train_model
