"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
import os
N_DIR = 'north_data'
n_file = 'customers_data.csv'
file_name_os = os.path.join(N_DIR, n_file)
conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="9090"
)
cur = conn.cursor()

with open(file_name_os, "r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            l = list(line.values())
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", l)

n_file = 'employees_data.csv'
file_name_os = os.path.join(N_DIR, n_file)
with open(file_name_os, "r") as file:
    reader = csv.DictReader(file)
    for line in reader:
        l = list(line.values())
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", l)

n_file = 'orders_data.csv'
file_name_os = os.path.join(N_DIR, n_file)
with open(file_name_os, "r") as file:
    reader = csv.DictReader(file)
    for line in reader:
        l = list(line.values())
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", l)

conn.commit()
cur.close()
conn.close()
