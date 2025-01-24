#!/usr/bin/env python
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="userDGL", port=5432)
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

cur.execute("""--sql
            CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
            );
""")

cur.execute("""--sql
            INSERT INTO person (id, name, age, gender) VALUES 
            (1, 'Mike', 30, 'm'),
            (2, 'Lisa', 30, 'f'),
            (3, 'John', 54, 'm'),
            (4, 'Bob', 80, 'm'),
            (5, 'Julie', 40, 'f');
""")

conn.commit()

cur.close()
conn.close()