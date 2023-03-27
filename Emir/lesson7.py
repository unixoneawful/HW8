import sqlite3

db = sqlite3.connect('test.db')
c = db.cursor()
c.execute('''CREATE TABLE user()''')