from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Collectibles Portal"
    admin_email: str = ""

    class Config:
        env_file = ".env"
