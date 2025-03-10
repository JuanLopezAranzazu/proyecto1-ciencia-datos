from db.database import engine, Base, SessionLocal
from sqlalchemy.sql import text
from models.dim_product import DimProduct
from models.dim_customer import DimCustomer
from models.dim_date import DimDate
from models.dim_payment_method import DimPaymentMethod
from models.dim_shopping_mall import DimShoppingMall
from models.fact_invoice import FactInvoice
from utils.load_data import load_db
from utils.create_graphs import generate_graphs

def main():
  # crear las tablas en la base de datos
  try:
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente")
  except Exception as e:
    print("Error al crear las tablas:", e)

  # crear una sesión de la base de datos
  db = SessionLocal()

  # verificar que la sesión está activa
  try:
    db.execute(text("SELECT 1"))
    print("Conexión exitosa")
  except Exception as e:
    print(e)
    print("Conexión fallida")

  # cargar los datos en las tablas
  load_db(db)
  # generar gráficas de los datos
  generate_graphs(db)

if __name__ == "__main__":
  main()
  