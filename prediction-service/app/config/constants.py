from pathlib import Path

SERVICE_PREFIX = "/prediction-service"
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

MODEL_PATHS = {
    "small": BASE_DIR / "models" / "address_model_sm",
    "medium": BASE_DIR / "models" / "address_model_md",
    "large": BASE_DIR / "models" / "address_model_lg",
}
