



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

-- create function

CREATE FUNCTION GetTotalPayments ( @start_date DATE,  @end_date DATE)

RETURNS DECIMAL(10, 2)
AS
BEGIN
    DECLARE @total_payments DECIMAL(10, 2)
    
    SELECT @total_payments = SUM(payment)
    FROM [Order]
    WHERE ordered_at BETWEEN @start_date AND @end_date

    RETURN ISNULL(@total_payments, 0)
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




