# install MySQL server
# ubuntu terminal
# sudo apt update (make sure all the packages are up to date)
# sudo apt install mysql-server
# mysql --version (confirm that mysql has been installed)

# sudo mysql_secure_installation (mysql set up)
# New Password: nick.mysql

# sudo mysql -u root (go to mysql console)
# mysql-> show databases;
# mysql-> create database linuxhint; # create a new database
# mysql-> quit # bye


"""
Install MySQL Driver
Python needs a MySQL driver to access the MySQL database.

In this tutorial we will use the driver "MySQL Connector".

We recommend that you use PIP to install "MySQL Connector".

PIP is most likely already installed in your Python environment.

Navigate your command line to the location of PIP, and type the following:

Download and install "MySQL Connector":

windows:
    C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install
    mysql-connector-python
linux:
    $ sudo apt update
    $ python3 -m pip install mysql-connector-python
"""




