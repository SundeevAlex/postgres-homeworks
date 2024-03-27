"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os

PASSWORD_KEY = os.getenv('MY_PASSWORD_KEY')


# заполние таблицы "employees" данными

with psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password=PASSWORD_KEY
) as connection:

    with connection.cursor() as cursor:
        with open('north_data\\employees_data.csv') as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:

                query = """INSERT INTO employees
                VALUES (%s, %s, %s, %s, %s, %s)"""

                cursor.execute(query, row)

connection.close()


# заполние таблицы "customers" данными

with psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password=PASSWORD_KEY
) as connection:

    with connection.cursor() as cursor:
        with open('north_data\\customers_data.csv') as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:

                query = """INSERT INTO customers
                VALUES (%s, %s, %s)"""

                cursor.execute(query, row)

connection.close()


# заполние таблицы "orders" данными

with psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password=PASSWORD_KEY
) as connection:

    with connection.cursor() as cursor:
        with open('north_data\\orders_data.csv') as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:

                query = """INSERT INTO orders 
                VALUES (%s, %s, %s, %s, %s)"""

                cursor.execute(query, row)

connection.close()
