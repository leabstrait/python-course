import sqlite3


conn = sqlite3.connect(':memory:')


c = conn.cursor()


# Create db

try:
    c.execute(""" create table employees (
                    id    integer primary key,
                    fname text,
                    lname text,
                    salary integer)
    """)
except sqlite3.OperationalError:
    print("table already exists, so skipping creation")


# Insert to db

c.execute(f"""
    INSERT INTO employees VALUES (1, "Labin", "Ojha", 300000)
""")
c.execute("""
    Insert into employees values (?, ?, ?, ?)
""", (2, "Darshan", "Gautam", 300000))
c.execute("""
    insert into employees values (:id, :fname, :lname, :salary)
""", {'fname': "Aman",
        'lname': "Ansari",
        'salary': 300000,
        'id': 3
    })

# Read from db
c.execute("""
    select * from employees where lname="Ansari"
""")
print(c.fetchone())

c.execute("""
    select * from employees where lname=:last
""", {'last': 'Gautam'})

print(c.fetchall())

# Update db

c.execute("""
    select fname, salary from employees where lname="Ojha"
""")
print(c.fetchall())

c.execute("""
    update employees set salary = 400000 
        where fname = "Labin"
""")
# print(c.fetchall())

c.execute("""
    select fname, salary from employees where lname="Ojha"
""")
print(c.fetchall())
######################################################



c.execute("""
    select * from employees where lname="Ojha"
""")
print(c.fetchall())

c.execute("""
    update employees set fname = "Gopal" 
        where id = 1
""")

c.execute("""
    update employees set lname = "KC" 
        where id = 1
""")


c.execute("""
    select * from employees where lname="Ojha"
""")
print(c.fetchall())

c.execute("""
    select * from employees where lname="KC"
""")
print(c.fetchall())

######################################################

# delete from db

c.execute(""" select * from employees""")
print(c.fetchall())

c.execute("""
    delete from employees where id = 2
""")

def remove_emp_by_fl(first, last):
    with conn:
        c.execute("""DELETE FROM employees WHERE fname = :first AND lname = :last""",
        {'first': first, 'last': last})

def remove_emp_by_id(id):
    with conn:
        c.execute("""DELETE FROM employees WHERE id = ? """, (id,))

remove_emp_by_fl('Aman', 'Ansari')
remove_emp_by_id(1)


# Class -> Django(ORM) -> CRUD

c.execute(""" select * from employees""")
print(c.fetchall())




conn.commit()

conn.close()