-- Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser`
-- that computes and store the average score for a student
-- An average score can be a decimal
-- Procedure `ComputeAverageScoreForUser` is taking 1 input:
-- `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing users)

DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE tot_score INT DEFAULT 0;
	DECLARE avg_score FLOAT DEFAULT 0.0;
	DECLARE cnt_score INT DEFAULT 0;

	SELECT SUM(score), COUNT(*) INTO tot_score, cnt_score
	FROM corrections
	WHERE corrections.user_id = user_id;

	IF tot_score > 0 THEN
		SET avg_score = CAST(tot_score AS DECIMAL) / cnt_score;
	ELSE
		SET avg_score = 0;
	END IF;

	UPDATE users
	SET users.average_score = avg_score
	WHERE users.id = user_id;
END; //
DELIMITER ;
