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

# Functions 

def insert_emp(first, last, pay):
    with conn:
        c.execute("""INSERT INTO employees VALUES (?, ?, ?)""", (first, last, pay))

def get_emps_by_lastname(last):
    c.execute("""SELECT * FROM employees WHERE last=? """, (last,))
    return c.fetchall()
    # no context manager because select doesn't need commiting

def update_pay(first, last, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                    {'first': first, 'last': last, 'pay': pay})

def remove_emp(first, last):
    with conn:
        c.execute("""DELETE FROM employees WHERE first = :first AND last = :last""",
        {'first': first, 'last': last})

# Insert to dB

insert_emp('Labin', 'Ojha', 300000)
insert_emp('Harry', 'Smith', 200000)
insert_emp('Adam', 'Smith', 100000)

# Query dB

print(get_emps_by_lastname('Ojha'))
print(get_emps_by_lastname('Smith'))

# Update dB

update_pay("Labin", "Ojha", 500000)
# View result of update
print(get_emps_by_lastname('Ojha'))

# Remove entry from dB

remove_emp("Labin", "Ojha")
# View result of delete
print(get_emps_by_lastname('Ojha'))

conn.close()

# NOTE: SQLite also works with SQLAlchemy, an ORM
# Hence, we can prototype with SQLAlchemy and SQLite
# and later replace with postgres or something