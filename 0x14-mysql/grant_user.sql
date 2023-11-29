-- creates user: holberton_user
-- hostname: localhost
-- password: projectcorrection280hbtn
-- grant the user replication prigiledge
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
