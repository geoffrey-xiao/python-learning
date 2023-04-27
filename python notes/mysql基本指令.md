## 登陆mysql



> mysql -u root -p 

```doubilei@bogon ~ % mysql.server start
Starting MySQL

 SUCCESS! 

doubilei@bogon ~ % 2021-10-02T01:33:18.6NZ mysqld_safe A mysqld process already exists

mysql -u root -p

Enter password: 

Welcome to the MySQL monitor. Commands end with ; or \g.

Your MySQL connection id is 9

Server version: 8.0.26 Homebrew



Copyright (c) 2000, 2021, Oracle and/or its affiliates.



Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.



Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```



## 查看了mysql中所有的库

> show databases;

```
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)
```



## 选择需要的库，打开库

> use mysql;



##  查看当前库中所有的表

> show tables;

```
mysql> show tables;
+------------------------------------------------------+
| Tables_in_mysql                                      |
+------------------------------------------------------+
| columns_priv                                         |
| component                                            |
| db                                                   |
| default_roles                                        |
| engine_cost                                          |
| func                                                 |
| general_log                                          |
| global_grants                                        |
| gtid_executed                                        |
| help_category                                        |
| help_keyword                                         |
| help_relation                                        |
| help_topic                                           |
| innodb_index_stats                                   |
| innodb_table_stats                                   |
| password_history                                     |
| plugin                                               |
| procs_priv                                           |
| proxies_priv                                         |
| replication_asynchronous_connection_failover         |
| replication_asynchronous_connection_failover_managed |
| replication_group_configuration_version              |
| replication_group_member_actions                     |
| role_edges                                           |
| server_cost                                          |
| servers                                              |
| slave_master_info                                    |
| slave_relay_log_info                                 |
| slave_worker_info                                    |
| slow_log                                             |
| tables_priv                                          |
| time_zone                                            |
| time_zone_leap_second                                |
| time_zone_name                                       |
| time_zone_transition                                 |
| time_zone_transition_type                            |
| user                                                 |
+------------------------------------------------------+
37 rows in set (0.00 sec)
```



## 查看表中的数据

> select * from user;
>
> select host, user from user;

```
mysql> select host,user from user;
+-----------+------------------+
| host      | user             |
+-----------+------------------+
| localhost | mysql.infoschema |
| localhost | mysql.session    |
| localhost | mysql.sys        |
| localhost | root             |
+-----------+------------------+
4 rows in set (0.00 sec)
```



## 创建自己的库

>  create database person default charset=utf8;



## 创建自己的表

```
use person;

create table student(

  -> name varchar(20),

  -> age int,

  -> sex char(1)

  -> )engine=innodb default chartset=utf8;
```





## 添加一些数据

> insert into studenet(name,age,sex) values('admin',20,'男');

```
mysql> insert into studenet(name,age,sex) values('admin',20,'男');
Query OK, 1 row affected (0.00 sec)

mysql> select * from studenet;
+-------+------+------+
| name  | age  | sex  |
+-------+------+------+
| admin |   20 | 男   |
+-------+------+------+
1 row in set (0.00 sec)
```



## 删除库

> drop database 库名；



## 查看表结构

> desc 表名；

```
mysql> desc studenet;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| name  | varchar(20) | YES  |     | NULL    |       |
| age   | int         | YES  |     | NULL    |       |
| sex   | char(1)     | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)
```



## 查看建表语句

> show create table student;

```
| studenet | CREATE TABLE `studenet` (
  `name` varchar(20) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `sex` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 |
```



## 修改表结构

#### 添加字段

```mysql
# 在users表中追加一个num字段
alter table users add num int not null;

#在指定位置追加email字段
alter table users add email varchar(15) after age;

#在表开头添加pid字段
alter table users add pid int first;

```

#### 删除字段

```
alter table users drop pid;
```

#### 修改字段

```mysql
# 不能修改字段名 modify
alter table users modify num tinyint not null default 12;

# 可以修改字段名 change 不推荐使用
alter table users change num nums int;

```

#### 修改表名

```mysql
#不推荐使用
alter table users rename as user;
```

#### 更改表中的自增值

```mysql
# 在默认情况下，auto_increment默认从1开始递增;
alter table users auto_increment=100;
```

#### 修改表引擎

```mysql
#推荐在定义表时，表引擎为innodb;还有myisam;

#修改表引擎 不推荐使用
alter table user engine='myisam'

#查看当前表引擎
show create table user;

Table: user
Create Table: CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(6) NOT NULL,
  `age` tinyint DEFAULT NULL,
  `email` varchar(15) DEFAULT NULL,
  `sex` enum('男','女') DEFAULT NULL,
  `nums` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3
1 row in set (0.00 sec)

#查看表的所有状态信息
show table status from person where name='user';

       Name: user
         Engine: InnoDB
        Version: 10
     Row_format: Dynamic
           Rows: 2
 Avg_row_length: 8192
    Data_length: 16384
Max_data_length: 0
   Index_length: 0
      Data_free: 0
 Auto_increment: 4
    Create_time: 2021-10-02 15:23:33
    Update_time: NULL
     Check_time: NULL
      Collation: utf8_general_ci
       Checksum: NULL
 Create_options: 
        Comment: 
1 row in set (0.00 sec)

```





![image](https://api2.mubu.com/v3/document_image/a1d7a60c-f206-4ef6-bd22-8cbd0b05ba8a-9404487.jpg)
