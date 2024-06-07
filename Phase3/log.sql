-- Create Log tables

CREATE TABLE InsertLog (
    log_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    table_name NVARCHAR(255) NOT NULL,
    changed_data NVARCHAR(MAX),
    changed_at DATETIME DEFAULT GETDATE()
);
CREATE TABLE DeleteLog (
    log_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    table_name NVARCHAR(255) NOT NULL,
    changed_data NVARCHAR(MAX), 
    changed_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE UpdateLog (
    log_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    table_name NVARCHAR(255) NOT NULL,
    previous_data NVARCHAR(MAX),
    changed_data NVARCHAR(MAX),
    changed_at DATETIME DEFAULT GETDATE()
);

-- Create Triggers

-- Insert Trigger for Employee
CREATE TRIGGER trg_Insert_Employee
ON Employee
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Employee', @json);
END;

-- Delete Trigger for Employee
CREATE TRIGGER trg_Delete_Employee
ON Employee
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Employee', @json);
END;

-- Update Trigger for Employee
CREATE TRIGGER trg_Update_Employee
ON Employee
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Employee', @previous_json, @changed_json);
END;


-- Insert Trigger for Chef
CREATE TRIGGER trg_Insert_Chef
ON Chef
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Chef', @json);
END;

-- Delete Trigger for Chef
CREATE TRIGGER trg_Delete_Chef
ON Chef
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Chef', @json);
END;

-- Update Trigger for Chef
CREATE TRIGGER trg_Update_Chef
ON Chef
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Chef', @previous_json, @changed_json);
END;



-- Insert Trigger for Waiter
CREATE TRIGGER trg_Insert_Waiter
ON Waiter
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Waiter', @json);
END;

-- Delete Trigger for Waiter
CREATE TRIGGER trg_Delete_Waiter
ON Waiter
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Waiter', @json);
END;

-- Update Trigger for Waiter
CREATE TRIGGER trg_Update_Waiter
ON Waiter
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Waiter', @previous_json, @changed_json);
END;




-- Insert Trigger for Shipper
CREATE TRIGGER trg_Insert_Shipper
ON Shipper
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Shipper', @json);
END;

-- Delete Trigger for Shipper
CREATE TRIGGER trg_Delete_Shipper
ON Shipper
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Shipper', @json);
END;

-- Update Trigger for Shipper
CREATE TRIGGER trg_Update_Shipper
ON Shipper
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Shipper', @previous_json, @changed_json);
END;





-- Insert Trigger for Manager
CREATE TRIGGER trg_Insert_Manager
ON Manager
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Manager', @json);
END;

-- Delete Trigger for Manager
CREATE TRIGGER trg_Delete_Manager
ON Manager
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Manager', @json);
END;

-- Update Trigger for Manager
CREATE TRIGGER trg_Update_Manager
ON Manager
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Manager', @previous_json, @changed_json);
END;






-- Insert Trigger for Customer
CREATE TRIGGER trg_Insert_Customer
ON Customer
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Customer', @json);
END;

-- Delete Trigger for Customer
CREATE TRIGGER trg_Delete_Customer
ON Customer
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Customer', @json);
END;

-- Update Trigger for Customer
CREATE TRIGGER trg_Update_Customer
ON Customer
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Customer', @previous_json, @changed_json);
END;









-- Insert Trigger for Table
CREATE TRIGGER trg_Insert_Table
ON [Table]
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Table', @json);
END;

-- Delete Trigger for Table
CREATE TRIGGER trg_Delete_Table
ON [Table]
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Table', @json);
END;

-- Update Trigger for Table
CREATE TRIGGER trg_Update_Table
ON [Table]
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Table', @previous_json, @changed_json);
END;







-- Insert Trigger for Order
CREATE TRIGGER trg_Insert_Order
ON [Order]
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Order', @json);
END;

-- Delete Trigger for Order
CREATE TRIGGER trg_Delete_Order
ON [Order]
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Order', @json);
END;

-- Update Trigger for Order
CREATE TRIGGER trg_Update_Order
ON [Order]
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Order', @previous_json, @changed_json);
END;







-- Insert Trigger for Item
CREATE TRIGGER trg_Insert_Item
ON Item
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Item', @json);
END;

-- Delete Trigger for Item
CREATE TRIGGER trg_Delete_Item
ON Item
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Item', @json);
END;

-- Update Trigger for Item
CREATE TRIGGER trg_Update_Item
ON Item
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Item', @previous_json, @changed_json);
END;






-- Insert Trigger for Order_Item
CREATE TRIGGER trg_Insert_Order_Item
ON Order_Item
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Order_Item', @json);
END;

-- Delete Trigger for Order_Item
CREATE TRIGGER trg_Delete_Order_Item
ON Order_Item
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Order_Item', @json);
END;

-- Update Trigger for Order_Item
CREATE TRIGGER trg_Update_Order_Item
ON Order_Item
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Order_Item', @previous_json, @changed_json);
END;









-- Insert Trigger for Recipe
CREATE TRIGGER trg_Insert_Recipe
ON Recipe
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Recipe', @json);
END;

-- Delete Trigger for Recipe
CREATE TRIGGER trg_Delete_Recipe
ON Recipe
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Recipe', @json);
END;

-- Update Trigger for Recipe
CREATE TRIGGER trg_Update_Recipe
ON Recipe
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Recipe', @previous_json, @changed_json);
END;













-- Insert Trigger for Item_Recipe
CREATE TRIGGER trg_Insert_Item_Recipe
ON Item_Recipe
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Item_Recipe', @json);
END;

-- Delete Trigger for Item_Recipe
CREATE TRIGGER trg_Delete_Item_Recipe
ON Item_Recipe
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Item_Recipe', @json);
END;

-- Update Trigger for Item_Recipe
CREATE TRIGGER trg_Update_Item_Recipe
ON Item_Recipe
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Item_Recipe', @previous_json, @changed_json);
END;









-- Insert Trigger for chef_Recipe
CREATE TRIGGER trg_Insert_chef_Recipe
ON chef_Recipe
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('chef_Recipe', @json);
END;

-- Delete Trigger for chef_Recipe
CREATE TRIGGER trg_Delete_chef_Recipe
ON chef_Recipe
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('chef_Recipe', @json);
END;

-- Update Trigger for chef_Recipe
CREATE TRIGGER trg_Update_chef_Recipe
ON chef_Recipe
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('chef_Recipe', @previous_json, @changed_json);
END;






-- Insert Trigger for Ingredient
CREATE TRIGGER trg_Insert_Ingredient
ON Ingredient
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Ingredient', @json);
END;

-- Delete Trigger for Ingredient
CREATE TRIGGER trg_Delete_Ingredient
ON Ingredient
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Ingredient', @json);
END;

-- Update Trigger for Ingredient
CREATE TRIGGER trg_Update_Ingredient
ON Ingredient
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Ingredient', @previous_json, @changed_json);
END;










-- Insert Trigger for Recipe_Ingredient
CREATE TRIGGER trg_Insert_Recipe_Ingredient
ON Recipe_Ingredient
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Recipe_Ingredient', @json);
END;

-- Delete Trigger for Recipe_Ingredient
CREATE TRIGGER trg_Delete_Recipe_Ingredient
ON Recipe_Ingredient
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Recipe_Ingredient', @json);
END;

-- Update Trigger for Recipe_Ingredient
CREATE TRIGGER trg_Update_Recipe_Ingredient
ON Recipe_Ingredient
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Recipe_Ingredient', @previous_json, @changed_json);
END;





-- Insert Trigger for Storehouse
CREATE TRIGGER trg_Insert_Storehouse
ON Storehouse
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Storehouse', @json);
END;

-- Delete Trigger for Storehouse
CREATE TRIGGER trg_Delete_Storehouse
ON Storehouse
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Storehouse', @json);
END;

-- Update Trigger for Storehouse
CREATE TRIGGER trg_Update_Storehouse
ON Storehouse
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Storehouse', @previous_json, @changed_json);
END;








-- Insert Trigger for Storehouse_Ingredient
CREATE TRIGGER trg_Insert_Storehouse_Ingredient
ON Storehouse_Ingredient
AFTER INSERT
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO InsertLog (table_name, changed_data)
    VALUES ('Storehouse_Ingredient', @json);
END;

-- Delete Trigger for Storehouse_Ingredient
CREATE TRIGGER trg_Delete_Storehouse_Ingredient
ON Storehouse_Ingredient
AFTER DELETE
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);
    
    SELECT @json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO DeleteLog (table_name, changed_data)
    VALUES ('Storehouse_Ingredient', @json);
END;

-- Update Trigger for Storehouse_Ingredient
CREATE TRIGGER trg_Update_Storehouse_Ingredient
ON Storehouse_Ingredient
AFTER UPDATE
AS
BEGIN
    DECLARE @previous_json NVARCHAR(MAX);
    DECLARE @changed_json NVARCHAR(MAX);
    
    SELECT @previous_json = (
        SELECT *
        FROM deleted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );
    
    SELECT @changed_json = (
        SELECT *
        FROM inserted
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    );

    INSERT INTO UpdateLog (table_name, previous_data, changed_data)
    VALUES ('Storehouse_Ingredient', @previous_json, @changed_json);
END;
