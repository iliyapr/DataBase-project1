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
