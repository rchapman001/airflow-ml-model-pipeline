from pathlib import Path

SERVICE_PREFIX = "/scraper-service"
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DATASET_PATHS = {
    "small": {
        "input": DATA_DIR / "in_popular_usa_zip_codes_sm.csv",
        "output": DATA_DIR / "out_popular_usa_zip_codes_sm.json",
    },
    "medium": {
        "input": DATA_DIR / "in_popular_usa_zip_codes_md.csv",
        "output": DATA_DIR / "out_popular_usa_zip_codes_md.json",
    },
    "large": {
        "input": DATA_DIR / "in_popular_usa_zip_codes_lg.csv",
        "output": DATA_DIR / "out_popular_usa_zip_codes_lg.json",
    },
}
