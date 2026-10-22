# config.py
from os import environ
from pathlib import Path
from pydantic import BaseModel, Field

raw_config_path = environ.get("CONFIG_PATH")
if not raw_config_path:
    raise RuntimeError("CRITICAL: Environment variable 'CONFIG_PATH' is not set.")
config_path = Path(raw_config_path)
if not config_path.is_file():
    raise FileNotFoundError(f"CRITICAL: Config file '{config_path}' does not exist.")

def get_secret(key: str) -> str:
    cred_dir = environ.get("CREDENTIALS_DIRECTORY")
    if not cred_dir:
        raise FileNotFoundError(f"CREDENTIALS_DIRECTORY environment variable not set.")
    
    secret_path = Path(cred_dir) / key
    if not secret_path.is_file():
        raise FileNotFoundError(f"Secret '{key}' not found in credentials directory.")
    
    val = secret_path.read_text(encoding="utf-8").strip()
    if not val:
        raise ValueError(f"Secret '{key}' is empty in credentials directory.")

    return val

            

class DatabaseConfig(BaseModel):
    host: str
    port: int
    name: str
    user: str
    password: str = ""

    def model_post_init(self, __context):
        if not self.password:
            self.password = get_secret("db_password")

class Config(BaseModel):
    node_id: int
    site_name: str
    log_path: str
    hosts: list[str] = Field(default_factory=lambda: ["127.0.0.1", "localhost"])
    port: int = 8000
    database: DatabaseConfig
    min_name_length: int = 1
    max_name_length: int = 255
    cookie_name: str
    pepper: str = ""
    session_secret: str = ""

    def model_post_init(self, __context):
        if not self.pepper:
            self.pepper = get_secret("pepper")
        if not self.session_secret:
            self.session_secret = get_secret("session_secret")
        # TODO: add error checking


def _load_config() -> Config:
    with open(config_path, "r", encoding="utf-8") as f:
        return Config.model_validate_json(f.read())




# Instantiated once when the module is imported
settings = _load_config()

