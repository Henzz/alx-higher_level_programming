-- List all privileges of the MYSQL users of 'user_0d_1'
-- and 'user_0d_2'
USER1='user_od_1'
USER2='user_od_2'
SELECT *
FROM mysql.user
WHERE user IN ('$USER1', '$USER2');
