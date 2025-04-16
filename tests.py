import psycopg2
from scripts import *
import requests
import os
import dotenv
import json

dotenv.load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

ADDR = "http://localhost:8000"
CAPLEN = 25

def printf(name, test, status):
    print(name + str(test).rjust(CAPLEN - len(name), " "), "|", status)

def testf(name):
    print("=" * 50)
    ln = 50 - len(name) - 2
    print("*" * (ln // 2), name + ("" if ln % 2 == 0 else " "), "*" * (ln // 2))

def check_req(r, test_cap, test_id, status) -> bool:
    if r.status_code == status:
        printf(test_cap, test_id, f"ok     {r.status_code}: {r.text}")
    else:
        printf(test_cap, test_id, f"failed {r.status_code}: {r.text}")
    return r.status_code == status

def test(test_id: int, caption: str, sequent: list) -> bool:
    testf(caption)
    SQL_init_schema(cur)
    printf("init", test_id, "ok")

    verdict = True
    for req in sequent:
        if req["method"] == "get":
            r = requests.get(f"{ADDR}{req['endpoint']}", json=req["body"])
        if req["method"] == "post":
            r = requests.post(f"{ADDR}{req['endpoint']}", json=req["body"])
        if req["method"] == "put":
            r = requests.put(f"{ADDR}{req['endpoint']}", json=req["body"])
        if not check_req(r, req["caption"], test_id, req["result"]):
            verdict = False
            break

    SQL_drop_all_shit(cur, confirm=True, warnings=False)
    printf("clean", test_id, "ok")

    return verdict


if __name__ == "__main__":
    conn = psycopg2.connect(host=DB_HOST,
                            port=DB_PORT,
                            database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASSWORD)
    conn.autocommit = True
    cur = conn.cursor()
    SQL_drop_all_shit(cur, confirm=True, warnings=False)
    printf("clean", 0, "ok")

    with open("tests.json", "r") as f:
        j = json.loads(f.read())
    
    for t in j:
        if not test(**t): break