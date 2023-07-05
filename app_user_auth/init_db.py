import sqlite3


# Run to Crush databse

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


with open("database.sql", "r") as sql_file:
    cursor.executescript(sql_file.read())
conn.commit()
conn.close()
