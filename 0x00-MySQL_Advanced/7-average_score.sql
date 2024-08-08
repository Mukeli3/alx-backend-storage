-- SQL script that creates a stored procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average_score DECIMAL(10, 2);

    -- Calculate the user average score
    SELECT AVG(score) INTO average_score
    FROM corrections
    WHERE user_id = user_id;

    -- update the average score in user_avgs table
    INSERT INTO user_avgs (user_id, average_score)
    VALUES (user_id, average_score)
    ON DUPLICATE KEY UPDATE average_score = average_score;

END $$

DELIMITER ;

