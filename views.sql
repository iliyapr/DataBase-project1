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




