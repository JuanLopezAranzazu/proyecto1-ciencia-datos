import os
from dotenv import load_dotenv

load_dotenv()

# variables de entorno
class GlobalConfig:
  def __init__(self):
    self.DB_USER = os.environ.get("DB_USER")
    self.DB_PASSWORD = os.environ.get("DB_PASSWORD")
    self.DB_HOST = os.environ.get("DB_HOST", "localhost")
    self.DB_PORT = int(os.environ.get("DB_PORT", 5432))
    self.DB_NAME = os.environ.get("DB_NAME")

global_config = GlobalConfig()
