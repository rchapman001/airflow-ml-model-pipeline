import requests
from app.config.settings import get_settings
import json
from datetime import datetime, timezone


def get_airflow_token():
    token_url = f"{get_settings().AIRFLOW_BASE}/auth/token"
    payload = {
        "username": get_settings().AIRFLOW_USERNAME,
        "password": get_settings().AIRFLOW_PASSWORD,
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    resp = requests.post(token_url, data=json.dumps(payload), headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.json()["access_token"]


def trigger_dag(dag_id: str, conf: dict | None = None):
    """
    Trigger any DAG.
    logical_date is always generated here.
    """
    token = get_airflow_token()

    logical_date = datetime.now(timezone.utc).isoformat()

    dag_url = f"{get_settings().AIRFLOW_BASE}/api/v2/dags/{dag_id}/dagRuns"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    payload = {
        "logical_date": logical_date,
        "conf": conf or {},
    }

    resp = requests.post(
        dag_url,
        headers=headers,
        data=json.dumps(payload),
        timeout=10,
    )

    resp.raise_for_status()
    return resp.json()
