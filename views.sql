CREATE VIEW daily_revenue
AS
SELECT
    o.orderd_at, SUM(oi.amount * i.price) AS total_sale
FROM 
    [Order] AS o
JOIN Order_Item AS oi
    ON o.id = oi.order_id 
JOIN Item AS i 
    ON i.id = oi.item_id
GROUP BY o.ordered_at
ORDER BY o.ordered_at DESC

GO

CREATE VIEW customers_with_the_most_orders
AS
SELECT 
    GetFullName(c.first_name, c.last_name), 
    total_paid, 
    total_orders
FROM Customer AS c 
JOIN
(SELECT TOP 1
	o.customer_id AS c_id, SUM(i.price * oi.amount) AS total_paid, COUNT(*) AS total_orders
FROM [Order] AS o
JOIN Order_Item AS oi
    ON oi.order_id = o.id
JOIN Item AS i
    ON i.id = oi.item_id
GROUP BY o.customer_id
ORDER BY total_orders DESC) AS max_orders
ON max_orders.c_id = c.id 


