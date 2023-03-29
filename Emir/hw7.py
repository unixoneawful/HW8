import sqlite3




db = sqlite3.connect('hw.db')

c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS

students(

name TEXT,

surname TEXT,

hobby TEXT,

b_date DATE,

mark Float

)''')




# c.execute('INSERT INTO students VALUES ("Жаннат", "Момуналиева","спать", "2003-05-07", 10.0)')

# c.execute('INSERT INTO students VALUES ("Эмиль", "Цой", "играть", "2003-04-13", 8.5)')

# c.execute('INSERT INTO students VALUES ("Дилназ", "Кайратбекова", "шить", "2003-08-23", 10.3)')

# c.execute('INSERT INTO students VALUES ("Акиса", "Имамова", "танцевать", "2002-04-20", 9.4)')

# c.execute('INSERT INTO students VALUES ("Шамиль", "Чернецов", "спать", "2003-12-17", 7.8)')

# c.execute('INSERT INTO students VALUES ("Санжар", "Асанов", "IOS", "2005-03-20", 10.6)')

# c.execute('INSERT INTO students VALUES ("Варя", "Панченко", "таэквондо", "2005-01-19", 7.0)')

# c.execute('INSERT INTO students VALUES ("Томирис", "Куменова", "есть", "2004-04-28", 8.1)')

# c.execute('INSERT INTO students VALUES ("Алина", "Ким", "дизайн", "2004-01-12", 6.9)')

# c.execute('INSERT INTO students VALUES ("Арина", "Ким", "готовить", "2004-01-12", 10.8)')




c.execute("SELECT rowid, * FROM students")

item = c.fetchall()

for i in item:

    print(i)




# c.execute("SELECT * FROM students WHERE length(surname) > 10")

# rows = c.fetchall()

# for row in rows:

#     print(row)




# c.execute("UPDATE students SET name = 'genius' WHERE mark > 10 ")

# c.execute("SELECT * FROM students WHERE name = 'genius'")

# item = c.fetchall()

# for i in item:

#     print(i)




c.execute("DELETE FROM students WHERE rowid % 2 = 0")




db.commit()

db.close()