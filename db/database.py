from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.global_config import global_config

# URL de la base de datos
DATABASE_URL = f"postgresql://{global_config.DB_USER}:{global_config.DB_PASSWORD}@{global_config.DB_HOST}:{global_config.DB_PORT}/{global_config.DB_NAME}"

# motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)

# sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base de datos para modelos
Base = declarative_base()
