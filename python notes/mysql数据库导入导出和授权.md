# MYSQL数据库导入导出和授权



## 数据导出

#### 1. 数据库数据导出

```shell
# 不要进入mysql,然后输入一下命令 到处某个库中的数据
mysqldump -u root -p person > ~/Desktop/python/person.sql
```

#### 2. 将数据库中的表导出

```shell
# 不要进入mysql,然后输入一下命令 到处某个库中的数据
mysqldump -u root -p person user > ~/Desktop/python/user.sql
```



## 数据导入

```
mysql -u root -p ops < ./user.sql
```



## 权限管理

```mysql
# grant 授权的操作 on 授权的库.授权的表 to 账户@登陆地址 indentified by 密码

grant select,insert on ops.* to zhangsan@'%' indentified by '123456';

grant select on person.* to zhangsan@'%' identified by '123456';

#mysql 8.0之后使用上面语句会报错 需要先执行下面的语句

# 使用mysql 数据库

mysql > use mysql;

# 特定用户的host 修改

mysql > update user set host='%' where user='root';

# 指定用户的授权

mysql > grant all privileges on test.* to root@'%'
```

