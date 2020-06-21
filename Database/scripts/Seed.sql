/*
	SEED Script Initial Categories
*/
DELETE FROM Categories;

INSERT INTO Categories (CategoryName) VALUES 
('Rent'),
('Student Loans'),
('Installment Loan'),
('Car Insurance'),
('Electricity'),
('Internet'),
('Emergency Savings'),
('Long Term Savings'),
('Short Term Savings'),
('Traditional IRA'),
('Cash'),
('Renters Insurance'),
('Spotify'),
('Netflix'),
('AMC A List'),
('Credit Card Payments'),
('Investments');

SELECT * FROM Categories ORDER BY CategoryName