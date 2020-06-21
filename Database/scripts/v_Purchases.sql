CREATE OR REPLACE VIEW v_Purchases AS SELECT 
	p.PK_PurchaseId,
    p.FK_CategoryId,
    c.CategoryName,
    p.Cost,
    p.Date
FROM Purchases p
INNER JOIN Categories c ON c.PK_CategoryId = p.FK_CategoryId;