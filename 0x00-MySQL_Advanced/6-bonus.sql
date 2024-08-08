-- SQL script that creates a stored procedure
DELIMITER $$
CREATE PROCEDURE AdBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score DECIMAL(10,2)
)
BEGIN
    DECLARE project_id INT;

    -- Check if the project exists
    SELECT id INTO project_ID
    FROM projects
    WHERE name = project_name;

    -- create if non-existant
    IF project_id IS NULL THEN
	INSERT INTO projects (name) VALUES (project_name);
	SET project_id = LAST_ID();
    END IF;

    -- Add student correction
    INSERT INTO correct (user_id, project_id, score) VALUES (user_id, project_id, score);
END $$
DELIMITER ;
