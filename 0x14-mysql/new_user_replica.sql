-- Create new user
-- Name: replica_user
-- Hostname: %
-- Password: projectcorrection280hbtn_1
-- Permissions: To replicate MySQL server

CREATE USER 'replica_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn_1';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;
