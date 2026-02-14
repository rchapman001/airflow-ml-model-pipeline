from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl
from functools import lru_cache
import os

ENV = os.getenv("APP_ENV")


class Settings(BaseSettings):
    print("Loading settings for environment:", ENV)

    SERVICE_PREFIX: str
    AIRFLOW_BASE: AnyHttpUrl
    PREDICTION_SERVICE: AnyHttpUrl
    DAG_ID: str
    AIRFLOW_USERNAME: str
    AIRFLOW_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=f".env.{ENV}",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
