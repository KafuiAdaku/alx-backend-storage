-- SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.
-- Procedure `AddBonus` is taking 3 inputs (in this order):
-- `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing users)
-- `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
-- score, the score value for the correction

DELIMITER // ;
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE proj_num INT;
	DECLARE proj_id INT;

	SELECT COUNT(*) INTO proj_num FROM projects WHERE name = project_name;

	IF proj_num = 0 THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET proj_id = LAST_INSERT_ID();
	ELSE
		SELECT id INTO proj_id FROM projects WHERE name = project_name;
	END IF;

	INSERT INTO  corrections (user_id, project_id, score) VALUES(user_id, proj_id, score);
END; //
DELIMITER ; //
