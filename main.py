import psycopg2
from scripts import INIT_SCHEME

DB_HOST = '79.174.88.238'
DB_PORT = 15221
DB_NAME = 'school_db'
DB_USER = 'school'
DB_PASSWORD = 'School1234*'


conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
conn.autocommit = True

cur = conn.cursor()

INIT_SCHEME(cur)

cur.execute("SELECT * FROM blinov_oboldin.Order")

print(cur.fetchall())

cur.close()
conn.close()