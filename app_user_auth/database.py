import sqlite3


#Initialize DB and connect it to app

def query(sql):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    data = cursor.execute(sql)

    conn.commit()
    conn.close()
    return data

# query("INSERT INTO Currencies (id, name) VALUES (1, 'BTC');")
