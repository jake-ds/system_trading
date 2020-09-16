# system_trading

### DATA BASE SETTING
- MySQL install 
  - MySQL Download : https://dev.mysql.com/downloads/ 
  - reference : https://withcoding.com/26

- DBeaver install 
  - DBeaver Download : https://dbeaver.io/download/ 
    1) connect to database 
    2) choose MySQL 
    3) input Database, password, (MySQL default Port : 3306) 
    4) test connection -> error accrue : dbeaver unable to load authentication plugin 'caching_sha2_password' 
    -> have to change authentication method at MySQL Command Line Client. 
    insert <Alter USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'abc';> 
    (root = user name, abc = password)

### db_connect.ipynb
- DB Connecting
- Create Table
- Select Table 
