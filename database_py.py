import sqlite3


def select():
    connection = sqlite3.connect(
        "database.db")
    cursor = connection.cursor()
    rows = cursor.execute(
        "SELECT analyze from Analysis ORDER BY date DESC").fetchone()
    print(rows[0])
    return str(rows[0])


def insert(datTime, analyze):
    connection = sqlite3.connect(
        "database.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Analysis VALUES ('{datTime}', '{analyze}')")
    connection.commit()
