import os
import pandas as pd
from sqlalchemy.sql import func
import matplotlib.pyplot as plt
from models.dim_category import DimCategory
from models.dim_customer import DimCustomer
from models.dim_date import DimDate
from models.dim_payment_method import DimPaymentMethod
from models.dim_shopping_mall import DimShoppingMall
from models.fact_invoice import FactInvoice

# directorio
graphs_dir = "graphs"

# total de ventas por categoría de producto
def plot_sales_by_category(db):
  # obtener datos
  results = (
    db.query(
      DimCategory.name,
      func.sum(FactInvoice.price).label("total_sales")
    )
    .join(FactInvoice, DimCategory.id == FactInvoice.category_id)
    .group_by(DimCategory.name)
    .order_by(func.sum(FactInvoice.price).desc())
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["category", "total_sales"])

  # generar gráfica
  plt.figure(figsize=(10, 5))
  plt.bar(df["category"], df["total_sales"])
  plt.xlabel("Categoría")
  plt.ylabel("Ventas totales")
  plt.title("Ventas totales por categoría de producto")
  plt.xticks(rotation=45)
  plt.ticklabel_format(style="plain", axis="y")
  plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
  plt.tight_layout()

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "sales_by_category.png"))
  plt.close()


# metodos de pago más populares
def plot_popular_payment_methods(db):
  # obtener datos
  results = (
    db.query(
      DimPaymentMethod.name,
      func.count(FactInvoice.id).label("total_invoices")
    )
    .join(FactInvoice, DimPaymentMethod.id == FactInvoice.payment_method_id)
    .group_by(DimPaymentMethod.name)
    .order_by(func.count(FactInvoice.id).desc())
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["payment_method", "total_invoices"])

  # generar gráfica
  plt.figure(figsize=(10, 7))
  plt.pie(df["total_invoices"], labels=df["payment_method"], autopct='%1.1f%%', startangle=140)
  plt.title("Métodos de pago más populares")
  plt.axis('equal') 

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "popular_payment_methods.png"))
  plt.close()

# generar gráficas de los datos
def generate_graphs(db):
  # crear directorio si no existe
  if not os.path.exists(graphs_dir):
    os.makedirs(graphs_dir)

  # gráficas
  plot_sales_by_category(db)
  plot_popular_payment_methods(db)

  print("Gráficas generadas con éxito!")
