import datetime
import time
import sqlite3
import os



con = sqlite3.connect('/home/branka/test1/bets.db')
cur = con.cursor()

#os.chmod("bets.db", 0o777)

# sqlite allows primary key column to contain NULL values
# Create table

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS test_table (col1 int, col2 int)
    ''')
con.commit()

cur.execute(
    '''
    insert into test_table
    values
    (1,10)
    ''')



con.commit()
con.close()