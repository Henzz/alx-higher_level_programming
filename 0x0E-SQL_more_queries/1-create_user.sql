-- Creates MySQL server user user_0d_1 with all privileges

-- Create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant permission
GRANT ALL ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
