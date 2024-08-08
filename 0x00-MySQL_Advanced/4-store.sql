--  SQL script creates a trigger that decreases quantity
DELIMITER $$
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE item_id = NEW.item_id;
END $$
DELIMITER ;
