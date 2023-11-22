### installing mysql version 5.7

# the installation should be in my alx server web_01

# STEP 1
visit  dev.mysql.com and copy the public key
- create a filder xxx.key and PASTE the public key into it

# STEP 2
- run the folloeing: sudo apt-key add name_of_file.key
 -  you will get 
	$ OK

# STEP 3
- runt he following: sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

# STEP 4
- run the following: sudo apt-get update

# STEP 5
sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.31-0ubuntu0.20.04.2
  Version table:
     8.0.31-0ubuntu0.20.04.2 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
     8.0.31-0ubuntu0.20.04.1 500
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.40-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages

# STEP 6
run the following: 
	sudo apt-get install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y
