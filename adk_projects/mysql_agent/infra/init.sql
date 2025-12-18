CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

INSERT INTO employees (name, department, salary) VALUES
("Alice", "Engineering", 120000),
("Bob", "Engineering", 110000),
("Charlie", "HR", 70000),
("Diana", "Marketing", 90000),
("Evan", "Engineering", 105000);
