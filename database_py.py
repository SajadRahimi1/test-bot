import sqlite3


def select():
    connection = sqlite3.connect(
        "./database.db")
    cursor = connection.cursor()
    rows = cursor.execute(
        "SELECT analyze from Analysis ORDER BY date DESC").fetchall()
    print(rows)
    return str(rows)


def insert(datTime, analyze):
    connection = sqlite3.connect(
        "./database.db ")
    cursor = connection.cursor()
    cursor.execute(
        f"""INSERT INTO Analysis (
                         date,
                         [analyze]
                     )
                     VALUES (
                         '{datTime}',
                         '{analyze}'
                     );""").fetchone()
    connection.commit()


def all():
    connection = sqlite3.connect(
        "./database.db")
    cursor = connection.cursor()
    rows = cursor.execute(
        "SELECT name FROM sqlite_schema WHERE type IN ('table','view')").fetchall()
    print(rows)
    return str(rows)
