-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
    first_name varchar(15) NOT NULL,
    last_name varchar(15) NOT NULL,
    title varchar(30) NOT NULL,
    birth_date varchar(10) NOT NULL,
    notes text
);

CREATE TABLE customers
(
    customer_id varchar(15) PRIMARY KEY,
    company_name varchar(70) NOT NULL,
    contact_name varchar(60) NOT NULL
);

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
    customer_id varchar(15) REFERENCES customers(customer_id) NOT NULL,
    employee_id int REFERENCES employees(employee_id) NOT NULL,
    order_date varchar(10) NOT NULL,
    ship_city varchar(20) NOT NULL
);

SELECT * FROM employees
