-- Creates MySQL server user user_0d_1 with all privileges

-- Check if the user already exists
SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_1';

-- If the user already exists, exit the script
IF ROW_COUNT() > 0 THEN
    SELECT 'user_0d_1 already exists. No changes made.';
    LEAVE;
END IF;

-- Create user_0d_1 and grant all privileges
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- Display a success message
SELECT 'user_0d_1 created with all privileges.';
