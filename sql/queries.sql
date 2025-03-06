
-- total de ventas por categoria de producto
SELECT c.name as category, SUM(i.price) as total
FROM fact_invoice i
JOIN dim_category c ON i.category_id = c.id
GROUP BY c.name
ORDER BY total DESC;


-- metodos de pago mas utilizados
SELECT p.name as payment_method, COUNT(i.id) as total
FROM fact_invoice i
JOIN dim_payment_method p ON i.payment_method_id = p.id
GROUP BY p.name
ORDER BY total DESC;


-- total de ventas por metodo de pago
SELECT p.name as payment_method, SUM(i.price) as total
FROM fact_invoice i
JOIN dim_payment_method p ON i.payment_method_id = p.id
GROUP BY p.name
ORDER BY total DESC;


-- centros comerciales mas visitados
SELECT s.name as shopping_mall, COUNT(i.id) as total
FROM fact_invoice i
JOIN dim_shopping_mall s ON i.shopping_mall_id = s.id
GROUP BY s.name
ORDER BY total DESC;


-- total de ventas por centro comercial
SELECT s.name as shopping_mall, SUM(i.price) as total
FROM fact_invoice i
JOIN dim_shopping_mall s ON i.shopping_mall_id = s.id
GROUP BY s.name
ORDER BY total DESC;


-- clientes que mas compran
SELECT c.id as customer, SUM(i.price) as total
FROM fact_invoice i
JOIN dim_customer c ON i.customer_id = c.id
GROUP BY c.id
ORDER BY total DESC;


-- total de ventas por mes
SELECT d.month as month, SUM(i.price) as total
FROM fact_invoice i
JOIN dim_date d ON i.date_id = d.id
GROUP BY d.month
ORDER BY total DESC;


-- total de ventas por dia de la semana
SELECT d.day_of_week as day_of_week, SUM(i.price) as total
FROM fact_invoice i
JOIN dim_date d ON i.date_id = d.id
GROUP BY d.day_of_week
ORDER BY total DESC;
