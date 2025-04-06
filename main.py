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

    match SQL_register_user(cur, model):
        case 0: return Response("ok", status_code=201)
        case 1: return Response("this user exists", status_code=409)
        case _: return Response("internal error", status_code=500)

@app.get("/orders/get")
async def get_order(r: Request):
    body = await r.json()

    data = SQL_get_order(cur, body["id_order"])
    match len(data):
        case 0: return Response("gay?", status_code=404)
        case _: return JSONResponse(data, status_code=200)

@app.get("/orders/my")
async def get_my_order(r: Request):
    body = await r.json()

    data = SQL_get_my_orders(cur, body["id_user"])
    match len(data):
        case 0: return Response("gay?", status_code=404)
        case _: return JSONResponse(data, status_code=200)

@app.post("/orders/create")
async def create_order(r: Request):
    body = CreateOrderModel.load_(await r.json())

    match SQL_create_order(cur, body):
        case 0: return Response("ok", status_code=201)
        case 1: return Response("user doesnt exist", status_code=406)
        case _: return Response("internal error", status_code=500)

@app.put("/orders/update")
async def update_order(r: Request):
    body = OrderStatusModel.load_(await r.json())

    match SQL_update_order(cur, body):
        case 0: return Response("ok", status_code=200)
        case 1: return Response("not found", status_code=404)
        case _: return Response("internal error", status_code=500)

if __name__ == "__main__" or True:
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    conn.autocommit = True
    cur = conn.cursor()
    SQL_init_scheme(cur)

    # cur.close()
    # conn.close()