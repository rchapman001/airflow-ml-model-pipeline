from pathlib import Path

SERVICE_PREFIX = "/trainer-service"
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
N_ITER = 20
DATASET_PATHS = {
    "small": {
        "input": BASE_DIR / "data" / "out_popular_usa_zip_codes_sm.json",
        "output": BASE_DIR / "models" / "address_model_sm",
    },
    "medium": {
        "input": BASE_DIR / "data" / "out_popular_usa_zip_codes_md.json",
        "output": BASE_DIR / "models" / "address_model_md",
    },
    "large": {
        "input": BASE_DIR / "data" / "out_popular_usa_zip_codes_lg.json",
        "output": BASE_DIR / "models" / "address_model_lg",
    },
}
