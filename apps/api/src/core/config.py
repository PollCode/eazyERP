from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # App
    ENVIRONMENT: str = "development"
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    # DB
    DATABASE_URL: str              # pooler: postgresql://...@...:6543/postgres?pgbouncer=true
    DATABASE_URL_MIGRATIONS: str   # directa: postgresql://...@...:5432/postgres

    # Redis
    REDIS_URL: str                 # redis://localhost:6379/0  (o rediss:// en Upstash)

    # Auth
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    PASSWORD_RESET_EXPIRE_MINUTES: int = 60
    
settings = Settings()