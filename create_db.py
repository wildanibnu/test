import sqlite3

# DB 1: customers
conn1 = sqlite3.connect('db1.db')
c1 = conn1.cursor()
# CREATE TABLE IF NOT EXISTS custemers   
c1.execute('''
    CREATE TABLE IF NOT EXISTS part1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        jumlah TEXT
    )
''')
c1.execute("INSERT INTO part1 (name, email, jumlah) VALUES ('Alice', 'alice@example.com','000')")
conn1.commit()
conn1.close()

# DB 2: products
conn2 = sqlite3.connect('db2.db')
# CREATE TABLE IF NOT EXISTS products
c2 = conn2.cursor()
c2.execute('''
    CREATE TABLE IF NOT EXISTS part2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        jumlah TEXT
    )
''')
c2.execute("INSERT INTO part2 (name, email, jumlah) VALUES ('Alice', 'alice@example.com','000')")
conn2.commit()
conn2.close()

# DB 3: orders
conn3 = sqlite3.connect('db3.db')
c3 = conn3.cursor()
#  CREATE TABLE IF NOT EXISTS orders
c3.execute('''
    CREATE TABLE IF NOT EXISTS part3  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        jumlah TEXT
    )
''')
c3.execute("INSERT INTO part3 (name, email, jumlah) VALUES ('Alice', 'alice@example.com','000')")
conn3.commit()
conn3.close()

# DB 4: part4
conn4 = sqlite3.connect('db4.db')
c4 = conn4.cursor()
#  CREATE TABLE IF NOT EXISTS orders
c4.execute('''
    CREATE TABLE IF NOT EXISTS part4  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        jumlah TEXT
    )
''')
c4.execute("INSERT INTO part4 (name, email, jumlah) VALUES ('Alice', 'alice@example.com','000')")
conn4.commit()
conn4.close()

# DB 5: part5
conn5 = sqlite3.connect('db5.db')
c5 = conn5.cursor()
#  CREATE TABLE IF NOT EXISTS orders
c5.execute('''
    CREATE TABLE IF NOT EXISTS part5  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        jumlah TEXT
    )
''')
c5.execute("INSERT INTO part5 (name, email, jumlah) VALUES ('Alice', 'alice@example.com','000')")
conn5.commit()
conn5.close()

# DB 6: part6
conn6 = sqlite3.connect('db6.db')
c6 = conn6.cursor()
#  CREATE TABLE IF NOT EXISTS orders
c6.execute('''
    CREATE TABLE IF NOT EXISTS part6  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        jumlah TEXT
    )
''')
c6.execute("INSERT INTO part6 (name, email, jumlah) VALUES ('Alice', 'alice@example.com','000')")
conn6.commit()
conn6.close()

# DB 7: part7
conn7 = sqlite3.connect('db7.db')
c7 = conn7.cursor()
#  CREATE TABLE IF NOT EXISTS orders
c7.execute('''
    CREATE TABLE IF NOT EXISTS part7  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        jumlah TEXT
    )
''')
c7.execute("INSERT INTO part7 (name, email, jumlah) VALUES ('Alice', 'alice@example.com','000')")
conn7.commit()
conn7.close()

# DB 8: part8
conn8 = sqlite3.connect('db8.db')
c8 = conn8.cursor()
#  CREATE TABLE IF NOT EXISTS orders
c8.execute('''
    CREATE TABLE IF NOT EXISTS part8  (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        jumlah TEXT
    )
''')
c8.execute("INSERT INTO part8 (name, email, jumlah) VALUES ('Alice', 'alice@example.com','000')")
conn8.commit()
conn8.close()

print("✅ 8 database berhasil dibuat siap pakai.")
