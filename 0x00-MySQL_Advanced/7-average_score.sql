-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Compute the average score for the given user_id
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Check if the user_id already exists in the average_scores table
    IF EXISTS (SELECT 1 FROM average_scores WHERE user_id = user_id) THEN
        -- Update the existing record with the new average score
        UPDATE average_scores
        SET average_score = avg_score
        WHERE user_id = user_id;
    ELSE
        -- Insert a new record with the user_id and the computed average score
        INSERT INTO average_scores (user_id, average_score)
        VALUES (user_id, avg_score);
    END IF;
END //

DELIMITER ;
