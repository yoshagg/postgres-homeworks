"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="armchair"
)

with conn.cursor() as cur:
    customers = './north_data/customers_data.csv'
    employees = './north_data/employees_data.csv'
    orders = './north_data/orders_data.csv'
    with open(customers, encoding="windows-1251") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(f"""INSERT INTO customers VALUES({row["customer_id"]}, {row["company_name"]}, {row["contact_name"]})""")
    with open(employees, encoding="windows-1251") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(f"""INSERT INTO employees VALUES({row["employee_id"]}, {row["first_name"]}, {row["last_name"]}, {row["title"]}, {row["birth_date"]}, {row["notes"]})""")
    with open(orders, encoding="windows-1251") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(f"""INSERT INTO orders VALUES({row["order_id"]},{row["customer_id"]}, {row["employee_id"]}, {row["order_date"]}, {row["ship_city"]})""")
    rows = cur.fetchall()
