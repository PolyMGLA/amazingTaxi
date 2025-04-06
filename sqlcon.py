import psycopg2
import os
import dotenv
from scripts import *

dotenv.load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
conn.autocommit = True
cur = conn.cursor()

while True:
    com = input(">> ")
    fetch = False
    if len(com) > 0 and com[0] == "!":
        fetch = True
        com = com[1:]

    if com == "q": break

    cur.execute(com)
    if fetch:
        if cur.pgresult_ptr is None:
            print("nothing to fetch")
        else:
            print(cur.fetchall())