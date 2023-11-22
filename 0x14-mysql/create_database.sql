-- Create the database
CREATE DATABASE tyrell_corp;

-- Use the database
USE tyrell_corp;

-- Create the table
CREATE TABLE nexus6 (
    id INT,
    name VARCHAR(25),
    class VARCHAR(12)
);

-- Insert data into the table
INSERT INTO nexus6 (id, name, class) VALUES (1, 'Magdaline Njuguna', 'Customer');
INSERT INTO nexus6 (id, name, class) VALUES (2, 'Cigi', 'Vendor');

-- Grant SELECT permissions to holberton_user
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

-- Select all rows from the table
SELECT * FROM nexus6;
