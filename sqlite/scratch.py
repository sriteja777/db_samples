import sqlite3
import time
import datetime
import random
import matplot
conn = sqlite3.connect('database.db')

c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuff(unix REAL, datestamp TEXT, keyword TEXT, value REAL )')
def data_entry():
    c.execute("INSERT INTO stuff VALUES(16736764, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuff (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()


def read_from_db():
    c.execute('SELECT * FROM stuff WHERE value=3 AND keyword="Python" AND unix > 1522960981')
    # data = c.fetchall()
    #print(data)
    for i in c.fetchall():
        print(i)


read_from_db()

#create_table()
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)
c.close()
conn.close()

#create_table()
 #data_entry()
