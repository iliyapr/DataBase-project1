CREATE TABLE Employees (
	ssn NCHAR(10) PRIMARY KEY,
	first_name NVARCHAR(30) NOT NULL,
	last_name NVARCHAR(30) NOT NULL,
	resume TEXT,
	address NVARCHAR(MAX),
	phone_number NCHAR(11) NOT NULL,
	started_at DATE NOT NULL,
	bank_account_number NCHAR(16),
	[role] NVARCHAR(30)
)
GO
