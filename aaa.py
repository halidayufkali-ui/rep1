import psycopg2
from connect import connect 

conn = connect()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS grades  
""")