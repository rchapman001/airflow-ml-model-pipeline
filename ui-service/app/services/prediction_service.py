import requests
from app.config.settings import get_settings


def predict(text: str, size: str):
    url = f"{get_settings().PREDICTION_SERVICE}/predict-address?size={size}"
    r = requests.post(url, json={"text": text}, timeout=30)
    r.raise_for_status()
    return r.json()
