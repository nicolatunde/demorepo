import sqlite3
connect = sqlite3.connect('my_sql_database.db')

cursor = connect.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender char(1) not null check(gender in ('m','f'))
    );
'''
)
# cursor.execute('''
#     insert into students (name, age, gender) values 
#                ('dada tunde', 27, 'm'),
#                ('akin willaims', 27, 'm'),
#                ('dele willis', 39, 'm');
# ''')
# connect.commit()

# cursor.execute('''
#     insert into students (name, age, gender) values 
#                ('dele akinvo', 58, 'f');
             
# ''')
# connect.commit()
# cursor.execute('''
#     delete from students where id = 2;
             
# ''')
# connect.commit()

# cursor.execute('SELECT * FROM students')

# rows = cursor.fetchall()

# for row in rows:
# #     print(row)

# cursor.execute('SELECT * FROM students where id = 1')
# row = cursor.fetchone()
# ident,name,age,sex = row
# print(row)
# print(ident)

# cursor.execute('SELECT name FROM students where id = 1')
# row = cursor.fetchone()
# print(row)
name = input("enter name:")
age = input("enter age:")
gender = input("enter gender (m/f): ")

cursor.execute('''
    INSERT into students (name, age, gender) values 
'''
    
)