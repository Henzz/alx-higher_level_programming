-- Creates MySQL server user user_0d_1 with all privileges

DELIMITER $$

CREATE PROCEDURE create_user_procedure()
BEGIN
	-- Select the desired database
	USE mysql;

	DECLARE user_exists BOOLEAN DEFAULT 0;

	-- Check if the user already exists
	SELECT COUNT(*) INTO user_exists FROM mysql.user WHERE user = 'user_0d_1';

	-- If the user already exists, exit the script
	IF user_exists != 0 THEN
		SELECT 'user_0d_1 already exists. No changes made.' AS message;
	ELSE
		-- Create user_0d_1 and grant all privileges
		CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
		GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

		-- Flush privileges to apply changes
		FLUSH PRIVILEGES;

		-- Display a success message
		SELECT 'user_0d_1 created with all privileges.' AS message;
	END IF;
END
$$

-- Set the delimiter back to the default semicolon
DELIMITER ;

-- Call the sored precedure to create the user
CALL create_user_procedure();
