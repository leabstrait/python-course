import sqlite3

# conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')

c = conn.cursor()

# Create dB

c.execute(""" CREATE TABLE employees (
            first text,
            last text,
            pay integer)
        """)

# Insert to dB

c.execute("""INSERT INTO employees VALUES ("Labin", "Ojha", 3000000)""")

c.execute("""INSERT INTO employees VALUES (?, ?, ?)""", ('Harry', 'Smith', 200000))
c.execute("""INSERT INTO employees VALUES (:first, :last, :pay)""", {'first': 'Adam', 'last': 'Smith', 'pay': 200000})

# Query dB

c.execute("""SELECT * FROM employees WHERE last="Ojha" """)
print(c.fetchone())

c.execute("""SELECT * FROM employees WHERE last=:last """, {'last': 'Smith'})
print(c.fetchall())

conn.commit()

conn.close()
