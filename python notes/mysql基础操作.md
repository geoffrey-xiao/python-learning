# mysql基础操作

### SQL(structure query language) 结构化查询语言

>SQL语言分为4部分：DDL（定义）,DML（操作）,DQL（查询）,DCL（控制）

### SQL语句中的快捷键

\G

```
create table if not exists users(
    -> id int not null primary key auto_increment,
    -> name varchar(6) not null,
    -> age tinyint,
    -> sex enum('男','女')
    -> )engine=innodb default charset=utf8;
```



### sql增删改查

```
# 插入数据
insert into users values (null,'李娜',30,'女');

#更新数据
update users set age=66,sex='女' where id=1;

#查询数据
select * from users where id=1;

#删除数据
 delete from users where id=3;
```



### mysql中的统计函数（聚合函数）

```mysql
# max(),min(),sum(),avg(),count()

select max(age),min(age),sum(age),avg(age) from user;
+----------+----------+----------+----------+
| max(age) | min(age) | sum(age) | avg(age) |
+----------+----------+----------+----------+
|       66 |       18 |      201 |  33.5000 |
+----------+----------+----------+----------+

select max(age) as age_max, min(age) as age_min, sum(age) as age_sum, avg(age) as age_avg from user;
+---------+---------+---------+---------+
| age_max | age_min | age_sum | age_avg |
+---------+---------+---------+---------+
|      66 |      18 |     201 | 33.5000 |
+---------+---------+---------+---------+

select count(*) from user;
+----------+
| count(*) |
+----------+
|        6 |
+----------+

select count(id) from user;
+-----------+
| count(id) |
+-----------+
|         6 |
+-----------+

```



### group by分组

```mysql
select sex,count(*) from user group by sex;
+------+----------+
| sex  | count(*) |
+------+----------+
| 女   |        3 |
| 男   |        3 |
+------+----------+

select sex,classid,count(*) from user group by sex,classid;
+------+---------+----------+
| sex  | classid | count(*) |
+------+---------+----------+
| 女   |       1 |        2 |
| 男   |       1 |        1 |
| 男   |       2 |        2 |
| 女   |       2 |        1 |
+------+---------+----------+
```

having子句是在分组聚合计算之后，对结果再一次进行过滤，类似于where

where过滤的是行数据，having过滤的是分组数据

```mysql
select classid,count(*) as num from user group by classid having num >3;
```



### order by排序

```mysql
#默认asc 升序， desc降序

select * from user order by age;

#降序
select * from user order by age desc;

#部分升序
select * from user order by age,id;

#部分升序 部分降序
select * from user order by age, id desc;
```



### limit数据分页

```mysql
#limit 3 提取3条数据
#limit 4,3 跳过4条数据 提取3条数据

select * from user limit 3;

select * from user limit 2,3;
```



### 总结

```mysql
# 一定要注意sql的正确性和顺序
select * from user where id>3 group by sex order by classid limit 4,3;
 
```

