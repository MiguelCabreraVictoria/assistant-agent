from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    langfuse_secret_key: str
    langfuse_public_key: str
    langfuse_base_url: str

    model: str

    class Config:
        env_file = ".env"

settings = Setting()