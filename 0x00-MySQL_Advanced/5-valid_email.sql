-- SQL script creates a trigger that resets attributes
DELIMITER $$
CREATE TRIGGER reset_mail
BEFORE UPDATE ON users FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
	SET NEW.valid_email = FALSE;
    END IF;
END $$
DELIMITER ;
