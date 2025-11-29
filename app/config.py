from pydantic import BaseSettings


class Settings(BaseSettings):
    rag_config_path: str = "configs/rag_config.yaml"

    class Config:
        env_file = ".env"


settings = Settings()
