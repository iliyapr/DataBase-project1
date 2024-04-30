CREATE TABLE Employees (
	ssn NCHAR(10) PRIMARY KEY,
	first_name NVARCHAR(30) NOT NULL,
	last_name NVARCHAR(30) NOT NULL,
	birth_date DATE,
	address NVARCHAR(255),
	phone_number NCHAR(11) NOT NULL,
	gender INT,
	resume TEXT,
	bank_account_number NCHAR(16),
	started_at DATE NOT NULL,
	[role] NVARCHAR(30),
	status INT NOT NULL
)
GO

CREATE TABLE Chefs (
	ssn NCHAR(10) PRIMARY KEY,
	[style] NVARCHAR(50),
	uniform_size INT
)
GO


CREATE TABLE Waiters (
	ssn NCHAR(10) PRIMARY KEY,
	uniform_size INT
)
GO


CREATE TABLE Shippers (
	ssn NCHAR(10) PRIMARY KEY,
	vehicle_plate_number NCHAR(8) NOT NULL,
	vehicle_model NVARCHAR(50)
)
GO


CREATE TABLE Managers (
	ssn NCHAR(10) PRIMARY KEY,
	username NVARCHAR(50),
	password NVARCHAR(255),
	responsibitiy NVARCHAR(255) NOT NULL
)
GO


CREATE TABLE Customers (
	id BIGINT IDENTITY(1,1) PRIMARY KEY,
	phone_number NCHAR(11) NOT NULL UNIQUE,
	first_name NVARCHAR(30),
	last_name NVARCHAR(30),
	address NVARCHAR(255)
)
GO


CREATE TABLE Tables (
	[number] INT PRIMARY KEY,
	capacity INT NOT NULL,
	status INT NOT NULL
)
GO


CREATE TABLE Orders (
	id BIGINT IDENTITY(1,1) PRIMARY KEY,
	customer_id BIGINT NOT NULL,
	shipper_ssn NCHAR(11),
	waiter_ssn NCHAR(11),
	ordered_at DATE NOT NULL,
	discount INT,
	status INT NOT NULL,
	payment INT NOT NULL,
	order_type INT NOT NULL
)
GO




