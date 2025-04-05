import psycopg2
from scripts import *
from models import RegUserModel, CreateOrderModel
import fastapi
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
import dotenv
import logging
import os

dotenv.load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


logging.basicConfig(filename="logs.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
app = FastAPI()

@app.get("/ping")
async def ping():
    return Response("alive", status_code=200)

@app.post("/users/reg")
async def register(r: Request):
    model = RegUserModel.load_(await r.json())

    match REGISTER_USER(cur, model):
        case 0: return Response("ok", status_code=200)
        case 1: return Response("this user exists", status_code=400)
        case _: return Response("internal error", status_code=500)

@app.get("/orders/get")
async def get_order(r: Request):
    body = await r.json()

    data = GET_ORDER(cur, body["order_id"])
    match len(data):
        case 0: return Response("gay?", status_code=404)
        case _: return JSONResponse(data, status_code=200)

if __name__ == "__main__" or True:
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    conn.autocommit = True
    cur = conn.cursor()
    # DROP_ALL_SHIT(cur)
    INIT_SCHEME(cur)
    REGISTER_USER(cur, RegUserModel("Петров Петр Петрррр", "88005553535"))
    CREATE_ORDER(cur, CreateOrderModel(1, "Ленина 52", "Ленина 42"))
    cur.execute("SELECT * FROM blinov_oboldin.Users")
    logging.debug(cur.fetchall())

    # cur.close()
    # conn.close()