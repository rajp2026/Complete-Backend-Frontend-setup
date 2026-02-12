from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://postgres:1234@localhost:5432/raj_dev"

    # # JWT
    # SECRET_KEY: str
    # ALGORITHM: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int

    # # Email
    # EMAIL_HOST: str
    # EMAIL_PORT: int
    # EMAIL_USER: str
    # EMAIL_PASS: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Single instance
settings = Settings()
