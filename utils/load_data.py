import pandas as pd
from models.dim_product import DimProduct
from models.dim_customer import DimCustomer
from models.dim_date import DimDate
from models.dim_payment_method import DimPaymentMethod
from models.dim_shopping_mall import DimShoppingMall
from models.fact_invoice import FactInvoice

# directorio
csv_file = "./data/customer_shopping_data.csv"

# cargar datos del dataset
def load_data(file_path):
  return pd.read_csv(file_path)

# cargar datos de productos
def insert_products(db, dataFrame):
  if db.query(DimProduct).count() == 0:
    # obtener productos únicos
    products = [{"name": product} for product in dataFrame["category"].unique()]
    db.bulk_insert_mappings(DimProduct, products)

# cargar datos de metodos de pago
def insert_payment_methods(db, dataFrame):
  if db.query(DimPaymentMethod).count() == 0:
    payment_methods = [{"name": method} for method in dataFrame["payment_method"].unique()]
    db.bulk_insert_mappings(DimPaymentMethod, payment_methods)

# cargar datos de centros comerciales
def insert_shopping_malls(db, dataFrame):
  if db.query(DimShoppingMall).count() == 0:
    shopping_malls = [{"name": mall} for mall in dataFrame["shopping_mall"].unique()]
    db.bulk_insert_mappings(DimShoppingMall, shopping_malls)

# cargar datos de fechas
def insert_dates(db, dataFrame):
  if db.query(DimDate).count() == 0:
    # transformar la columna invoice_date a tipo fecha
    dataFrame['invoice_date'] = pd.to_datetime(dataFrame['invoice_date'], dayfirst=True)
    dates = [
      {
        "full_date": date,
        "day": date.day,
        "month": date.month,
        "year": date.year,
        "day_of_week": date.dayofweek
     }
      for date in dataFrame["invoice_date"].unique()
    ]
    db.bulk_insert_mappings(DimDate, dates)

# cargar datos de clientes
def insert_customers(db, dataFrame):
  if db.query(DimCustomer).count() == 0:
    customers = dataFrame[["customer_id", "gender", "age"]].drop_duplicates()
    customers_data = [
      {
        "id": row["customer_id"],
        "gender": row["gender"],
        "age": row["age"]
      }
      for _, row in customers.iterrows()
    ]
    db.bulk_insert_mappings(DimCustomer, customers_data)

# cargar datos de facturas
def insert_invoices(db, dataFrame):
  if db.query(FactInvoice).count() == 0:
    # mapear los IDs de las tablas relacionadas
    product_map = {p.name: p.id for p in db.query(DimProduct).all()}
    payment_map = {p.name: p.id for p in db.query(DimPaymentMethod).all()}
    mall_map = {m.name: m.id for m in db.query(DimShoppingMall).all()}
    customer_map = {c.id: c.id for c in db.query(DimCustomer).all()}
    date_map = {d.full_date: d.id for d in db.query(DimDate).all()}

    # crear una nueva columna con el total de la factura
    dataFrame["total_price"] = dataFrame["price"] * dataFrame["quantity"]

    # transformar la columna invoice_date a tipo fecha
    dataFrame['invoice_date'] = pd.to_datetime(dataFrame['invoice_date'], dayfirst=True)

    invoices_data = [
      {
        "id": row["invoice_no"],
        "customer_id": customer_map[row["customer_id"]],
        "product_id": product_map[row["category"]],
        "payment_method_id": payment_map[row["payment_method"]],
        "shopping_mall_id": mall_map[row["shopping_mall"]],
        "date_id": date_map[row["invoice_date"].date()],
        "quantity": row["quantity"],
        "unit_price": row["price"],
        "total_price": row["total_price"]
      }
      for _, row in dataFrame.iterrows()
    ]
    db.bulk_insert_mappings(FactInvoice, invoices_data)

# cargar datos en la base de datos
def load_db(db):
  dataFrame = load_data(csv_file)
   
  try:
    insert_products(db, dataFrame)
    insert_payment_methods(db, dataFrame)
    insert_shopping_malls(db, dataFrame)
    insert_customers(db, dataFrame)
    insert_dates(db, dataFrame)
    insert_invoices(db, dataFrame)

    # confirmar cambios
    db.commit()
    print("Datos insertados correctamente")
  except Exception as e:
    db.rollback()
    print(f"Error: {e}")

  finally:
    db.close()
    print("Conexión cerrada")
