-- crear bodega de datos

CREATE DATABASE IF NOT EXISTS data_warehouse;
USE data_warehouse;

-- tablas de dimensiones

CREATE TABLE IF NOT EXISTS dim_customer  (
  id VARCHAR PRIMARY KEY,
  gender VARCHAR,
  age INT
);

CREATE TABLE IF NOT EXISTS dim_product  (
  id SERIAL PRIMARY KEY,
  name VARCHAR
);

CREATE TABLE IF NOT EXISTS dim_payment_method  (
  id SERIAL PRIMARY KEY,
  name VARCHAR
);

CREATE TABLE IF NOT EXISTS dim_shopping_mall  (
  id SERIAL PRIMARY KEY,
  name VARCHAR
);

CREATE TABLE IF NOT EXISTS dim_date  (
  id SERIAL PRIMARY KEY,
  full_date DATE,
  day INT,
  month INT,
  year INT,
  day_of_week INT
);

-- tablas de hechos

CREATE TABLE IF NOT EXISTS fact_invoice  (
  id VARCHAR PRIMARY KEY,
  customer_id VARCHAR,
  product_id INT,
  payment_method_id INT,
  shopping_mall_id INT,
  date_id INT,
  quantity INT,
  unit_price DECIMAL(10, 2),
  total_price DECIMAL(10, 2),
  FOREIGN KEY (customer_id) REFERENCES dim_customer(id),
  FOREIGN KEY (product_id) REFERENCES dim_product(id),
  FOREIGN KEY (payment_method_id) REFERENCES dim_payment_method(id),
  FOREIGN KEY (shopping_mall_id) REFERENCES dim_shopping_mall(id),
  FOREIGN KEY (date_id) REFERENCES dim_date(id)
);
