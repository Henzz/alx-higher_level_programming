-- Converts 'hbtn_0c_0' DB to UTF8(utf8mb4,
-- collate utf8mb4_unicode_ci) in your MySQL server

-- Seleting the DB
USE hbtn_0c_0;

-- Converting
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
