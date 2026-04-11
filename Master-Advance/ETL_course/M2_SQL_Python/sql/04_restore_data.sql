-- 把四張表清空（保留 schema，只刪資料）
-- 練習時如果搞壞資料可以用這個 reset，再重跑 03_insert_data.sql
DELETE FROM scores;
DELETE FROM courses;
DELETE FROM teachers;
DELETE FROM students;
