
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
