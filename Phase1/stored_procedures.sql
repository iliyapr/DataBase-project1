-- create procedure 

CREATE PROCEDURE UpdateTableStatus (@order_id INT)
AS
BEGIN
    DECLARE @order_status INT
    DECLARE @table_number INT
    
    -- Get the order status and table ID from the Order table
    SELECT @order_status = [status], @table_number = table_number
    FROM [Order]
    WHERE id = @order_id
    
    -- Check if the order status is 0
    IF @order_status = 0
    BEGIN
        -- Update the table_status in the Table table to 0
        UPDATE [Table]
        SET [status] = 0
        WHERE number = @table_number
    END
END

GO

CREATE PROCEDURE IncreaseItemPrice (@item_id INT)
AS
BEGIN

    DECLARE @current_price INT

    SELECT @current_price = price
    FROM Item
    Where id = @item_id


    -- Increase item price in the Table Item by 10 percent
    UPDATE Item
    SET [price] = (@item_id * 1.1)
    WHERE number = @table_number
END

GO


CREATE PROCEDURE UpdateShipperStatus
    @order_id INT
AS
BEGIN
    DECLARE @status INT
    DECLARE @order_type INT
    DECLARE @shipper_ssn nchar(10)
    
    -- Get the order status, order type, and shipper ID from the Order table

    SELECT @status = [status] , @order_type = order_type, @shipper_ssn = shipper_ssn
    FROM [Order]
    WHERE id = @order_id
    
    -- Check if the order status is 0 and order type is 2

    IF @status = 0 AND @order_type = 2
    BEGIN
        -- Update the shipper_status in the Shipper table to 0

        UPDATE Employee
        SET [status] = 0
        WHERE ssn = @shipper_ssn

    END
END


-- create function

CREATE FUNCTION GetTotalPayments ( @start_date DATE,  @end_date DATE)

RETURNS INT
AS
BEGIN
    DECLARE @total_payments INT
    
    SELECT @total_payments = SUM(i.price * oi.amount)
    FROM [Order] AS o
	JOIN Order_Item AS oi
		ON o.id = oi.order_id
	JOIN Item AS i
		ON i.id = oi.item_id
    WHERE O.ordered_at BETWEEN @start_date AND @end_date

    RETURN ISNULL(@total_payments, 0)
END
GO


CREATE FUNCTION GetMeanRate ( @order_id INT)

RETURNS float
AS
BEGIN

    -- Calculate the mean rate for items in the specified order
    DECLARE @mean_rate FLOAT
    
    SELECT @mean_rate = AVG(CAST(rate AS FLOAT))
    FROM Order_Item
    WHERE order_id = @order_id

    RETURN @mean_rate
END
GO



CREATE FUNCTION GetMostPopularItems ( @start_date DATE,  @end_date DATE)

RETURNS TABLE
AS
RETURN
	SELECT TOP 1 Item.id, COUNT(*) AS cnt FROM [Order]
	JOIN Order_Item ON [Order].id = Order_Item.order_id
	JOIN Item ON Order_Item.item_id = Item.id
	WHERE [Order].ordered_at BETWEEN @start_date AND @end_date
	GROUP BY Item.id
	ORDER BY cnt DESC
GO


CREATE FUNCTION GetFullName ( @first_name NVARCHAR(30), @last_name NVARCHAR(30))

RETURNS NVARCHAR(61)
AS
BEGIN
    DECLARE @full_name NVARCHAR(61);
    
    SET @full_name = CONCAT(@first_name, ' ', @last_name);

    RETURN @full_name;
END
GO

-- create trigger

CREATE TRIGGER UpdateItemAmount
ON Order_Item
AFTER INSERT

AS
BEGIN

    -- Check if there are enough items in stock for the newly inserted order items
    IF EXISTS (
        SELECT *
        FROM inserted 
        JOIN Item ON inserted.item_id = Item.id
        WHERE Item.amount < inserted.amount
    )
    BEGIN
        -- Rollback the transaction if there are not enough items in stock
        ROLLBACK TRANSACTION;
        RAISERROR ('Not enough items in stock for the order. order cancelled.', 16, 1);
    END
    ELSE
    BEGIN
        -- Update the item stock based on the newly inserted order items
        UPDATE Item
        SET Item.amount = Item.amount - inserted.amount
        FROM Item
        JOIN inserted ON item.id = inserted.item_id;
    END

END

GO





