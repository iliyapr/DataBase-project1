-- View for Daily Insert Logs
CREATE VIEW vw_DailyInsertLog AS
SELECT 
    log_id,
    table_name,
    changed_data,
    changed_at
FROM InsertLog
WHERE CAST(changed_at AS DATE) = CAST(GETDATE() AS DATE);

GO

-- View for Daily Delete Logs
CREATE VIEW vw_DailyDeleteLog AS
SELECT 
    log_id,
    table_name,
    changed_data,
    changed_at
FROM DeleteLog
WHERE CAST(changed_at AS DATE) = CAST(GETDATE() AS DATE);

GO


-- View for Daily Update Logs
CREATE VIEW vw_DailyUpdateLog AS
SELECT 
    log_id,
    table_name,
    previous_data,
    changed_data,
    changed_at
FROM UpdateLog
WHERE CAST(changed_at AS DATE) = CAST(GETDATE() AS DATE);

GO

-- View for Employees

CREATE VIEW vw_Log_Employee AS
SELECT 
    'INSERT' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    InsertLog
WHERE 
    table_name = 'Employee'

UNION ALL

SELECT 
    'UPDATE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    previous_data,
    changed_at
FROM 
    UpdateLog
WHERE 
    table_name = 'Employee'

UNION ALL

SELECT 
    'DELETE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    DeleteLog
WHERE 
    table_name = 'Employee';

GO

-- View for Chef

CREATE VIEW vw_Log_Chef AS
SELECT 
    'INSERT' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    InsertLog
WHERE 
    table_name = 'Chef'

UNION ALL

SELECT 
    'UPDATE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    previous_data,
    changed_at
FROM 
    UpdateLog
WHERE 
    table_name = 'Chef'

UNION ALL

SELECT 
    'DELETE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    DeleteLog
WHERE 
    table_name = 'Chef';

GO

--View for Waiter

CREATE VIEW vw_Log_Waiter AS
SELECT 
    'INSERT' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    InsertLog
WHERE 
    table_name = 'Waiter'

UNION ALL

SELECT 
    'UPDATE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    previous_data,
    changed_at
FROM 
    UpdateLog
WHERE 
    table_name = 'Waiter'

UNION ALL

SELECT 
    'DELETE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    DeleteLog
WHERE 
    table_name = 'Waiter';


GO

--View for Shipper

CREATE VIEW vw_Log_Shipper AS
SELECT 
    'INSERT' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    InsertLog
WHERE 
    table_name = 'Shipper'

UNION ALL

SELECT 
    'UPDATE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    previous_data,
    changed_at
FROM 
    UpdateLog
WHERE 
    table_name = 'Shipper'

UNION ALL

SELECT 
    'DELETE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    DeleteLog
WHERE 
    table_name = 'Shipper';
GO

--View for manager

CREATE VIEW vw_Log_Manager AS
SELECT 
    'INSERT' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    InsertLog
WHERE 
    table_name = 'Manager'

UNION ALL

SELECT 
    'UPDATE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    previous_data,
    changed_at
FROM 
    UpdateLog
WHERE 
    table_name = 'Manager'

UNION ALL

SELECT 
    'DELETE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    DeleteLog
WHERE 
    table_name = 'Manager';

GO

--View for customer

CREATE VIEW vw_Log_Customer AS
SELECT 
    'INSERT' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    InsertLog
WHERE 
    table_name = 'Customer'

UNION ALL

SELECT 
    'UPDATE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    previous_data,
    changed_at
FROM 
    UpdateLog
WHERE 
    table_name = 'Customer'

UNION ALL

SELECT 
    'DELETE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    DeleteLog
WHERE 
    table_name = 'Customer';

GO

--View Order

CREATE VIEW vw_Log_Order AS
SELECT 
    'INSERT' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    InsertLog
WHERE 
    table_name = 'Order'

UNION ALL

SELECT 
    'UPDATE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    previous_data,
    changed_at
FROM 
    UpdateLog
WHERE 
    table_name = 'Order'

UNION ALL

SELECT 
    'DELETE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    DeleteLog
WHERE 
    table_name = 'Order';

GO

--View for Item

CREATE VIEW vw_Log_Item AS
SELECT 
    'INSERT' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    InsertLog
WHERE 
    table_name = 'Item'

UNION ALL

SELECT 
    'UPDATE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    previous_data,
    changed_at
FROM 
    UpdateLog
WHERE 
    table_name = 'Item'

UNION ALL

SELECT 
    'DELETE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    DeleteLog
WHERE 
    table_name = 'Item';

GO

--View for Recipe

CREATE VIEW vw_Log_Recipe AS
SELECT 
    'INSERT' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    InsertLog
WHERE 
    table_name = 'Recipe'

UNION ALL

SELECT 
    'UPDATE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    previous_data,
    changed_at
FROM 
    UpdateLog
WHERE 
    table_name = 'Recipe'

UNION ALL

SELECT 
    'DELETE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    DeleteLog
WHERE 
    table_name = 'Recipe';

GO

--View for Ingredient

CREATE VIEW vw_Log_Ingredient AS
SELECT 
    'INSERT' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    InsertLog
WHERE 
    table_name = 'Ingredient'

UNION ALL

SELECT 
    'UPDATE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    previous_data,
    changed_at
FROM 
    UpdateLog
WHERE 
    table_name = 'Ingredient'

UNION ALL

SELECT 
    'DELETE' AS change_type,
    log_id,
    table_name,
    changed_data AS data,
    NULL AS previous_data,
    changed_at
FROM 
    DeleteLog
WHERE 
    table_name = 'Ingredient';