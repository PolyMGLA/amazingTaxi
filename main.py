import psycopg2
from scripts import *
from models import RegUserModel, CreateOrderModel

DB_HOST = '79.174.88.238'
DB_PORT = 15221
DB_NAME = 'school_db'
DB_USER = 'school'
DB_PASSWORD = 'School1234*'

if __name__ == "__main__":
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    conn.autocommit = True

    cur = conn.cursor()
    # DROP_ALL_SHIT(cur)
    INIT_SCHEME(cur)
    REGISTER_USER(cur, RegUserModel("Петров Петр Петрррр", "88005553535"))
    CREATE_ORDER(cur, CreateOrderModel(1, "Ленина 52", "Ленина 42"))
    cur.execute("SELECT * FROM blinov_oboldin.Order")
    print(cur.fetchall())

    cur.close()
    conn.close()