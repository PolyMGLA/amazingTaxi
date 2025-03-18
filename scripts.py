import datetime
import psycopg2
from models import RegUserModel, CreateOrderModel

SCHEME_QUERY = "CREATE SCHEMA IF NOT EXISTS blinov_oboldin;"
TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS blinov_oboldin.Users
(
    id_user bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    fio text COLLATE pg_catalog."default" NOT NULL,
    telephone text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_pkey PRIMARY KEY (id_user),
    CONSTRAINT fio_telephone UNIQUE (fio, telephone)
);

CREATE TABLE IF NOT EXISTS blinov_oboldin.Taxi
(
    id_Taxi bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    CONSTRAINT "Taxi_pkey" PRIMARY KEY (id_Taxi)
);

CREATE TABLE IF NOT EXISTS blinov_oboldin.Driver
(
    id_dreiver bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    CONSTRAINT "Driver_pkey" PRIMARY KEY (id_dreiver)
);

CREATE TABLE IF NOT EXISTS blinov_oboldin.Shift
(
    id_shift bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    id_taxi bigint NOT NULL,
    id_driver bigint NOT NULL,
    date date NOT NULL,
    status text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Shift_pkey" PRIMARY KEY (id_shift)
);

CREATE TABLE IF NOT EXISTS blinov_oboldin.Order
(
    id_order bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    id_user bigint NOT NULL,
    id_shift bigint,
    start_addr text COLLATE pg_catalog."default" NOT NULL,
    end_addr text COLLATE pg_catalog."default" NOT NULL,
    order_time text COLLATE pg_catalog."default" NOT NULL,
    status text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Order_pkey" PRIMARY KEY (id_order)
);
"""

def INIT_SCHEME(cur):
    cur.execute(SCHEME_QUERY)
    cur.execute(TABLE_QUERY)

    if cur.pgresult_ptr is not None: print(cur.fetchall())

def DROP_ALL_SHIT(cur):
    """
    Дропает все данные, осторожно
    """
    k = input("Дропнуть? (y) ")
    if k != "y": return None
    cur.execute("DROP SCHEMA IF EXISTS blinov_oboldin CASCADE")

    if cur.pgresult_ptr is not None: print(cur.fetchall())


def REGISTER_USER(cur, model: RegUserModel) -> int:
    try:
        cur.execute(f"""
INSERT INTO blinov_oboldin.Users (fio, telephone) VALUES (\'{model.fio}\', {model.telephone});
        """)

        if cur.pgresult_ptr is not None: print(cur.fetchall())
        return 0
    except psycopg2.errors.UniqueViolation:
        print("прикол юзер уже зареган")
        return 1
    except Exception as e:
        print(e)
        return 2


def CREATE_ORDER(cur, model: CreateOrderModel) -> int:
    cur.execute(f"SELECT * FROM blinov_oboldin.Users WHERE Users.id_user={model.id_user}")
    if cur.pgresult_ptr is None or cur.fetchall() == []: return 1

    cur.execute(f"""
INSERT INTO blinov_oboldin.Order (id_user, start_addr, end_addr, order_time, status)
                VALUES ({model.id_user}, \'{model.start_addr}\', \'{model.end_addr}\', \'{datetime.datetime.now()}\', \'waiting\');
                """)
    if cur.pgresult_ptr is not None: print(cur.fetchall())

    return 0