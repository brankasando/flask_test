from pywebio.input import *
from pywebio.output import *

import pandas as pd
import sqlite3
from pywebio.output import put_html
from pywebio import pin

con = sqlite3.connect('bets.db')
cur = con.cursor()

q1 = '''
    select distinct col1 from test_table
    '''
cur.execute(q1)
list1 = cur.fetchall()
print(list(list1))

list_item = pin.put_select('input', options= [1,2])

print(list_item)
q2 = '''
    select * from test_table where col1 = col1
    '''

# records = cur.fetchall()

db_df = pd.read_sql_query(q2, con, params={'%col1':list_item})
df_html = db_df.to_html()
print(df_html)
# print("Total rows are:  ", len(records))

cur.close()
con.close()


put_html(df_html).send()
