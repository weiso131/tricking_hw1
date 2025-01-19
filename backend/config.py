from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    uri: str
    dc_name: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
