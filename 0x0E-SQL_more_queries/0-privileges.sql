-- List all privileges of the MYSQL users of 'user_0d_1'
-- and 'user_0d_2'
USER1='user_od_1'
USER2='user_od_2'

-- Query to retrieve privileges for USER1
SHOW GRANTS FOR '$USER1'@'localhost';

-- Query to retrieve privileges for USER2
SHOW GRANTS FOR '$USER2'@'localhost';
