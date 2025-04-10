'''Q1. What is a database? Differentiate between SQL and NoSQL databases.
A database is a structured collection of data that can be easily stored, managed, retrieved, and updated. Think of it like a digital filing cabinet 📁 where you can search, add, or update information quickly.'''

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = 'singlaji1'
)
cursor = conn.cursor()
cursor.execute(' CREATE DATABASE IF NOT EXISTS testdb')
conn.close()

conn = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'singlaji1',
    database= "testdb"
)



cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS students(id INT,name VARCHAR(255))')
cursor.execute("INSERT INTO students (id,name) VALUES(1,'Mayank')")
conn.commit()

cursor.execute('SELECT * FROM students')
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()  

# ✅ NoSQL Example (Using pymongo for MongoDB)

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['school']
students = db['students']

students.insert_one({'id':1,'name':'Mayank'})

for student in students.find():
    print(student)


'''Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

DDL stands for Data Definition Language.

It includes SQL commands that are used to define or modify the structure of a database — like creating tables, changing their structure, or deleting them.

Command	Purpose
CREATE	Create a new table or database
DROP	Delete a table or database completely
ALTER	Change the structure of a table
TRUNCATE	Delete all data from a table but keep the table'''

# 1. CREATE – To create a table

CREATE TABLE students( 
    id INT,
    name VARCHAR(100)
);

# 2. DROP – To delete the table completely

DROP TABLE students

# 3. ALTER – To modify the table (e.g., add a column)

ALTER TABLE students ADD email VARCHAR(100);

# 4. TRUNCATE – To delete all rows but keep the table

TRUNCATE TABLE students;


# Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
# DML stands for Data Manipulation Language.

# It includes SQL commands used to manipulate (change) the data inside existing tables. Unlike DDL, it doesn't affect the structure — only the data.
# Command	Purpose
# INSERT	Add new data into a table
# UPDATE	Modify existing data in a table
# DELETE	Remove data from a table



CREATE TABLE students(
    id INT,
    name VARCHAR(100),
    marks INT

);

# 1. INSERT – Add a new row
INSERT INTO students (id,name,marks) VALUES(1,'Mayank',85);

# 2. UPDATE – Change existing data
UPDATE students SET marks = 90 WHERE id =1;

# 3. DELETE – Remove a row
DELETE FROM students WHERE id=1;


'''Q4. What is DQL? Explain SELECT with an example.

DQL stands for Data Query Language.

It is used to query or fetch data from a database. Unlike DDL or DML, it doesn’t change the data — it only reads it.'''

#  1. Select all columns from a table

SELECT * FROM students;

#  2. Select specific columns

SELECT name,marks FROM students;

#  3. Select with condition

SELECT * FROM students WHERE marks>80;

'''Q5. Explain Primary Key and Foreign Key.


A Primary Key is a column (or a set of columns) that:

Uniquely identifies each row in a table

Cannot be NULL

Values must be unique

'''

CREATE TABLE students(
    students_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

# Here, student_id is the Primary Key — no two students can have the same student_id.

'''A Foreign Key is a column that:

Links one table to another

Refers to the Primary Key in another table

Helps maintain relational integrity'''

CREATE TABLE marks(
    mark_id INT PRIMARY KEY,
    student_id INT,
    marks INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)

);

'''Here, student_id in marks is a Foreign Key that links to the student_id in students.

This means:

You can’t insert a student_id in marks if it doesn't exist in students

Ensures valid relationships between tables'''

'''Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.'''

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='singlaji1',
    database = 'testdb'
)

cursor = conn.cursor()
cursor.execute('SELECT DATABASE();')

result = cursor.fetchone()
print('Connected to database',result)

conn.close()

'''
🔹 cursor()
This method creates a cursor object.

A cursor acts like a pointer that helps you execute SQL queries and fetch results.

It's similar to how a file pointer works when reading a file.


🔹 execute(sql_query)
This method is used to run an SQL command.

Can be used for:

SELECT, INSERT, UPDATE, DELETE

CREATE TABLE, etc.'''


'''Q7. Give the order of execution of SQL clauses in an SQL query.
🔢 Correct Order of Execution:
FROM – chooses the table to query

JOIN – (if used) combines tables

WHERE – filters rows before grouping

GROUP BY – groups rows with the same values

HAVING – filters groups (after grouping)

SELECT – selects columns and expressions

DISTINCT – removes duplicate rows

ORDER BY – sorts the result

LIMIT / OFFSET – limits number of rows returned
'''

SELECT name, COUNT(*) AS total_orders
FROM orders
WHERE status = 'shipped'
GROUP BY name
HAVING total_orders<5
ORDER BY total_orders DESC
LIMIT 10;








from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

config ={
    'host': 'localhost',
    'user': 'root',
    'password': 'singlaji1',
    'database': 'testdb'
}

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS students2 (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                marks INT
            )    
        ''')

        cursor.execute(" SELECT COUNT (*) FROM students2")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO students2 (id,name,marks) VALUES (1,'Mayank',90)")
            conn.commit()
            
        cursor.execute("SELECT * FROM students2")
        students2 = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template ('index.html',students2 = students2)
        
    except mysql.connector.Error as err:
        return f'Database Error: {err}'

if __name__ == "__main__":
    app.run(debug=True)














