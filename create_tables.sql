USE restaurant

CREATE TABLE Employee (
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
	status INT NOT NULL,
	
)
GO


CREATE TABLE Chef (
	ssn NCHAR(10) PRIMARY KEY,
	[style] NVARCHAR(50),
	uniform_size INT,
	FOREIGN KEY (ssn) REFERENCES Employee (ssn) 
		ON DELETE CASCADE
		ON UPDATE CASCADE
)
GO


CREATE TABLE Waiter (
	ssn NCHAR(10) PRIMARY KEY,
	uniform_size INT,
	FOREIGN KEY (ssn) REFERENCES Employee (ssn) 
		ON DELETE CASCADE 
		ON UPDATE CASCADE
)
GO


CREATE TABLE Shipper (
	ssn NCHAR(10) PRIMARY KEY,
	vehicle_plate_number NCHAR(8) NOT NULL,
	vehicle_model NVARCHAR(50),
	FOREIGN KEY (ssn) REFERENCES Employee (ssn) 
		ON DELETE CASCADE 
		ON UPDATE CASCADE
)
GO


CREATE TABLE Manager (
	ssn NCHAR(10) PRIMARY KEY,
	username NVARCHAR(50),
	password NVARCHAR(255),
	responsibitiy NVARCHAR(255) NOT NULL,
	FOREIGN KEY (ssn) REFERENCES Employee (ssn) 
		ON DELETE CASCADE
		ON UPDATE CASCADE
)
GO


CREATE TABLE Customer (
	id BIGINT IDENTITY(1,1) PRIMARY KEY,
	phone_number NCHAR(11) NOT NULL UNIQUE,
	first_name NVARCHAR(30),
	last_name NVARCHAR(30),
	address NVARCHAR(255)
)
GO


CREATE TABLE [Table] (
	number INT PRIMARY KEY,
	capacity INT NOT NULL,
	status INT NOT NULL
)
GO


CREATE TABLE [Order] (
	id BIGINT IDENTITY(1,1) PRIMARY KEY,
	customer_id BIGINT NOT NULL,
	shipper_ssn NCHAR(10),
	waiter_ssn NCHAR(10),
	table_number INT ,
	ordered_at DATE NOT NULL,
	discount INT,
	status INT NOT NULL,
	payment INT NOT NULL,
	order_type INT NOT NULL,
	
	FOREIGN KEY (customer_id) REFERENCES Customer (id) 
		ON UPDATE CASCADE,
		
    FOREIGN KEY (waiter_ssn) REFERENCES Waiter (ssn) 
		ON UPDATE CASCADE,

	FOREIGN KEY (shipper_ssn) REFERENCES Shipper (ssn) ,

	FOREIGN KEY (table_number) REFERENCES [Table] (number)
		ON UPDATE CASCADE
	     
)
GO





CREATE TABLE Item (
	id INT IDENTITY(1,1) PRIMARY KEY,
	title NVARCHAR(255) NOT NULL,
	cateorgy NVARCHAR(255),
	description TEXT,
	cooking BIT NOT NULL,
	price INT NOT NULL,
	amount INT NOT NULL
)
GO


CREATE TABLE Order_Item (
	order_id BIGINT NOT NULL,
	item_id INT NOT NULL,
	amount INT NOT NULL,
	rate INT,
	PRIMARY KEY (order_id, item_id),
	FOREIGN KEY (order_id) REFERENCES [Order] (id) 
		ON UPDATE CASCADE,
	FOREIGN KEY (item_id) REFERENCES [Item] (id) 
		ON UPDATE CASCADE
)
GO


CREATE TABLE Recipe (
	id INT IDENTITY(1,1) PRIMARY KEY,
	instructions TEXT
)
GO


CREATE TABLE Item_Recipe (
	item_id INT NOT NULL,
	recipe_id INT NOT NULL,
	
	PRIMARY KEY (item_id, recipe_id),
	FOREIGN KEY (item_id) REFERENCES [Item] (id) 
		ON UPDATE CASCADE,
	FOREIGN KEY (recipe_id) REFERENCES Recipe (id) 
		ON UPDATE CASCADE
)
GO


CREATE TABLE chef_Recipe (
	chef_ssn NCHAR(10) NOT NULL,
	recipe_id INT NOT NULL,
	
	PRIMARY KEY (chef_ssn, recipe_id),
	FOREIGN KEY (chef_ssn) REFERENCES Chef (ssn) 
		ON UPDATE CASCADE,
	FOREIGN KEY (recipe_id) REFERENCES Recipe (id) 
		ON UPDATE CASCADE
)
GO


CREATE TABLE Ingredient (
	id INT IDENTITY(1,1) PRIMARY KEY,
	name NVARCHAR(255),
	[type] NVARCHAR(255),
	unit NVARCHAR(10)
)
GO


CREATE TABLE Recipe_Ingredient (
	recipe_id INT NOT NULL,
	ingredient_id INT NOT NULL,
	amount INT,
	
	PRIMARY KEY (recipe_id, ingredient_id),
	FOREIGN KEY (recipe_id) REFERENCES Recipe (id) 
		ON UPDATE CASCADE,
	FOREIGN KEY (ingredient_id) REFERENCES Ingredient (id) 
		ON UPDATE CASCADE
)
GO


CREATE TABLE Storehouse (
	id INT IDENTITY(1,1) PRIMARY KEY,
	address NVARCHAR(255),
	manager_ssn NCHAR(10),

	FOREIGN KEY (manager_ssn) REFERENCES Manager (ssn)
		ON UPDATE CASCADE
)
GO


CREATE TABLE Storehouse_Ingredient (
	storehouse_id INT NOT NULL,
	ingredient_id INT NOT NULL,
	amount INT,
	
	PRIMARY KEY (storehouse_id, ingredient_id),
	FOREIGN KEY (storehouse_id) REFERENCES Storehouse (id)
		ON UPDATE CASCADE,
	FOREIGN KEY (ingredient_id) REFERENCES Ingredient (id)
		ON UPDATE CASCADE
)
GO









