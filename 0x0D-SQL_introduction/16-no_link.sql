-- Lists all records of the table
-- with the name value set
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
