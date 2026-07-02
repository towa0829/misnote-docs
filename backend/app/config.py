from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://misnote:misnote@localhost:5432/misnote"
    secret_key: str = "change-me-in-production"

    class Config:
        env_file = ".env"


settings = Settings()
