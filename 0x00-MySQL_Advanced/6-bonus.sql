-- SQL script that creates a stored procedure
DELIMITER $$
CREATE PROCEDURE AdBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;
    SELECT id INTO project_ID
    FROM projects
    WHERE name = project_name;
    IF project_id IS NOT NULL THEN
	INSERT INTO projects (name) VALUES (project_name);
	SET project_id = LAST_ID();
    END IF;
    INSERT INTO correct (user_id, project_id, score)
    VALUES (use_id, project_id, score);
END $$
DELIMITER ;
