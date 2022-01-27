from pydantic import BaseSettings, Field, validator

#local test database settings

class Settings(BaseSettings):
    env: str = Field("prod", env="ENV")
    app_url: str = Field("http://localhost:8000", env="APP_URL")
    db_uri: str = Field(
        "mysql+pymysql://pma:test1234@localhost:3306/accounts", env="DB_URI"
    )

    jwt_secret_key: str = Field("example_key_super_secret", env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field("HS256", env="JWT_ALGORITHM")

    class Config:
        env_file = '.env'


settings = Settings()