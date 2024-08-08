--  SQL script creates a trigger that decreases the quantity of an item after adding a new order.
DELIMITER $$

CREATE TRIGGER decrease_quant
AFTER INSERT ON orders FOR EACH ROW
BEGIN
    UPDATE items
    SET quant = quant - NEW.quant
    WHERE item_id = NEW.item_id;
END $$

DELIMITER ;
