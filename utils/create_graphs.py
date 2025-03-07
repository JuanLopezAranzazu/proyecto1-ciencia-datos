import os
import pandas as pd
from sqlalchemy.sql import func
import matplotlib.pyplot as plt
from models.dim_product import DimProduct
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
      DimProduct.name,
      func.sum(FactInvoice.total_price).label("total_sales")
    )
    .join(FactInvoice, DimProduct.id == FactInvoice.product_id)
    .group_by(DimProduct.name)
    .order_by(func.sum(FactInvoice.total_price).desc())
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


# total de ventas por metodo de pago
def plot_sales_by_payment_method(db):
  # obtener datos
  results = (
    db.query(
      DimPaymentMethod.name,
      func.sum(FactInvoice.total_price).label("total_sales")
    )
    .join(FactInvoice, DimPaymentMethod.id == FactInvoice.payment_method_id)
    .group_by(DimPaymentMethod.name)
    .order_by(func.sum(FactInvoice.total_price).desc())
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["payment_method", "total_sales"])

  # generar gráfica
  plt.figure(figsize=(10, 5))
  plt.bar(df["payment_method"], df["total_sales"])
  plt.xlabel("Método de pago")
  plt.ylabel("Ventas totales")
  plt.title("Ventas totales por método de pago")
  plt.xticks(rotation=45)
  plt.ticklabel_format(style="plain", axis="y")
  plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
  plt.tight_layout()

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "sales_by_payment_method.png"))
  plt.close()


# total de ventas por mes
def plot_sales_by_month(db):
  # obtener datos
  results = (
    db.query(
      DimDate.month,
      func.sum(FactInvoice.total_price).label("total_sales")
    )
    .join(FactInvoice, DimDate.id == FactInvoice.date_id)
    .group_by(DimDate.month)
    .order_by(DimDate.month)
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["month", "total_sales"])

  # generar gráfica
  plt.figure(figsize=(10, 5))
  plt.plot(df["month"], df["total_sales"], marker="o")
  plt.xlabel("Mes")
  plt.ylabel("Ventas totales")
  plt.title("Ventas totales por mes")
  plt.xticks(
    range(1, 13),
    ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    rotation=45
  )
  plt.ticklabel_format(style="plain", axis="y")
  plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
  plt.tight_layout()

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "sales_by_month.png"))
  plt.close()


# total de ventas por dia de la semana
def plot_sales_by_day_of_week(db):
  # obtener datos
  results = (
    db.query(
      DimDate.day_of_week,
      func.sum(FactInvoice.total_price).label("total_sales")
    )
    .join(FactInvoice, DimDate.id == FactInvoice.date_id)
    .group_by(DimDate.day_of_week)
    .order_by(DimDate.day_of_week)
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["day_of_week", "total_sales"])

  # generar gráfica
  plt.figure(figsize=(10, 5))
  plt.plot(df["day_of_week"], df["total_sales"], marker="o")
  plt.xlabel("Día de la semana")
  plt.ylabel("Ventas totales")
  plt.title("Ventas totales por día de la semana")
  plt.xticks(range(0, 7), ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
  plt.ticklabel_format(style="plain", axis="y")
  plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
  plt.tight_layout()

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "sales_by_day_of_week.png"))
  plt.close()


# centros comerciales mas populares
def plot_popular_shopping_malls(db):
  # obtener datos
  results = (
    db.query(
      DimShoppingMall.name,
      func.count(FactInvoice.id).label("total_invoices")
    )
    .join(FactInvoice, DimShoppingMall.id == FactInvoice.shopping_mall_id)
    .group_by(DimShoppingMall.name)
    .order_by(func.count(FactInvoice.id).desc())
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["shopping_mall", "total_invoices"])

  # generar gráfica
  plt.figure(figsize=(10, 7))
  plt.pie(df["total_invoices"], labels=df["shopping_mall"], autopct='%1.1f%%', startangle=140)
  plt.title("Centros comerciales más populares")
  plt.axis('equal') 

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "popular_shopping_malls.png"))
  plt.close()


# total de ventas por centro comercial
def plot_sales_by_shopping_mall(db):
  # obtener datos
  results = (
    db.query(
      DimShoppingMall.name,
      func.sum(FactInvoice.total_price).label("total_sales")
    )
    .join(FactInvoice, DimShoppingMall.id == FactInvoice.shopping_mall_id)
    .group_by(DimShoppingMall.name)
    .order_by(func.sum(FactInvoice.total_price).desc())
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["shopping_mall", "total_sales"])

  # generar gráfica
  plt.figure(figsize=(10, 5))
  plt.bar(df["shopping_mall"], df["total_sales"])
  plt.xlabel("Centro comercial")
  plt.ylabel("Ventas totales")
  plt.title("Ventas totales por centro comercial")
  plt.xticks(rotation=45)
  plt.ticklabel_format(style="plain", axis="y")
  plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
  plt.tight_layout()

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "sales_by_shopping_mall.png"))
  plt.close()


# total de ventas por genero
def plot_sales_by_gender(db):
  # obtener datos
  results = (
    db.query(
      DimCustomer.gender,
      func.sum(FactInvoice.total_price).label("total_sales")
    )
    .join(FactInvoice, DimCustomer.id == FactInvoice.customer_id)
    .group_by(DimCustomer.gender)
    .all()
  )

  # crear dataframe
  df = pd.DataFrame(results, columns=["gender", "total_sales"])

  # generar gráfica
  plt.figure(figsize=(10, 7))
  plt.pie(df["total_sales"], labels=df["gender"], autopct='%1.1f%%', startangle=140)
  plt.title("Ventas totales por género")
  plt.axis('equal') 

  # guardar gráfica
  plt.savefig(os.path.join(graphs_dir, "sales_by_gender.png"))
  plt.close()


# generar gráficas de los datos
def generate_graphs(db):
  # crear directorio si no existe
  if not os.path.exists(graphs_dir):
    os.makedirs(graphs_dir)

  # gráficas
  plot_sales_by_category(db)
  plot_popular_payment_methods(db)
  plot_sales_by_payment_method(db)
  plot_sales_by_month(db)
  plot_sales_by_day_of_week(db)
  plot_sales_by_shopping_mall(db)
  plot_popular_shopping_malls(db)
  plot_sales_by_gender(db)

  print("Gráficas generadas con éxito!")
