import sqlite3


def connect():
    conct = sqlite3.connect("Database.db")
    cur = conct.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Customers (id INTEGER PRIMARY KEY, name text, city text, country text)")
    cur.execute("CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, name text, price real, count INTEGER)")
    conct.commit()
    conct.close()


def insert(file_name):
    conct = sqlite3.connect("Database.db")
    cur = conct.cursor()
    with open(file_name, 'r') as file:
        queries = file.read().split(';')
    for query in queries:
        cur.execute(query)
    conct.commit()
    conct.close()


def view(file_name):
    conct = sqlite3.connect("Database.db")
    cur = conct.cursor()
    with open(file_name, 'r') as file:
        query = file.read()
    cur.execute(query)
    rows = cur.fetchall()
    conct.close()
    return rows


def delete(file_name):
    conct = sqlite3.connect("Database.db")
    cur = conct.cursor()
    with open(file_name, 'r') as file:
        query = file.read()
    cur.execute(query)
    conct.commit()
    conct.close()


def update(file_name):
    conct = sqlite3.connect("Database.db")
    cur = conct.cursor()
    with open(file_name, 'r') as file:
        query = file.read()
    cur.execute(query)
    conct.commit()
    conct.close()


connect()

insert("Query_1.sql")

data = view("Query_2.sql")
print(data)

delete("Query_3.sql")

update("Query_4.sql")
