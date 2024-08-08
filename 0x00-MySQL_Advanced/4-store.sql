--  SQL script creates a trigger that decreases quantity
DELIMITER $$
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE item = NEW.item_name;
END;
$$
DELIMITER ;
