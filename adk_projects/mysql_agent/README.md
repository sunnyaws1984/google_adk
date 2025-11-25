Command to get this MySQL Infra up:

Pre-req:
pip install sqlalchemy pymysql

Docker Commands:

docker compose down -v
docker compose up

```bash

$ docker exec -it <Container> sh
sh-5.1# mysql -h 127.0.0.1 -u root -p
Enter password:
...

mysql> USE company;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SELECT * FROM employees;
+----+---------+-------------+--------+
| id | name    | department  | salary |
+----+---------+-------------+--------+
|  1 | Alice   | Engineering | 120000 |
|  2 | Bob     | Engineering | 110000 |
|  3 | Charlie | HR          |  70000 |
|  4 | Diana   | Marketing   |  90000 |
|  5 | Evan    | Engineering | 105000 |
+----+---------+-------------+--------+
5 rows in set (0.01 sec)

```

Sample Query:

what is the salary of Alice ?
Alice is from which department ?
What is the Salary of Evan and he is from which department 