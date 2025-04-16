import datetime
import psycopg2
from models import RegUserModel, CreateOrderModel, OrderStatusModel
import logging

with open("migrations.sql", "r") as f:
    SCHEMA_QUERY = f.read()

__ALL__ = ["SQL_init_schema",
           "SQL_drop_all_shit",
           "SQL_register_user",
           "SQL_create_order",
           "SQL_get_order",
           "SQL_get_my_orders",
           "SQL_update_order"]

def SQL_init_schema(cur):
    cur.execute(SCHEMA_QUERY)
    logging.info("db initialized")

    if cur.pgresult_ptr is not None: logging.debug(cur.fetchall())

def SQL_drop_all_shit(cur, confirm: bool = False, warnings: bool = True):
    """
    Дропает все данные, осторожно
    """
    if not confirm: 
        k = input("Дропнуть? (y) ")
        if k != "y": return None
    cur.execute("DROP SCHEMA IF EXISTS blinov_oboldin CASCADE")
    if warnings: logging.warning("db dropped")

    if cur.pgresult_ptr is not None: logging.debug(cur.fetchall())

def SQL_register_user(cur, model: RegUserModel) -> int:
    try:
        cur.execute(f"""
INSERT INTO blinov_oboldin.Users (full_name, phone) VALUES (\'{model.full_name}\', {model.phone});
        """)

        if cur.pgresult_ptr is not None: logging.debug(cur.fetchall())
        return 0
    except psycopg2.errors.UniqueViolation:
        # logging.warning("прикол юзер уже зареган")
        return 1
    except Exception as e:
        logging.debug(e)
        return 2


def SQL_create_order(cur, model: CreateOrderModel) -> int:
    cur.execute(f"SELECT * FROM blinov_oboldin.Users WHERE blinov_oboldin.Users.id_user={model.id_user}")
    if cur.pgresult_ptr is None or cur.fetchall() == []: return 1

    cur.execute(f"""
INSERT INTO blinov_oboldin.Order (id_user, start_addr, end_addr, order_time, status)
                VALUES ({model.id_user}, \'{model.start_addr}\', \'{model.end_addr}\', \'{datetime.datetime.now()}\', \'waiting\');
                """)
    if cur.pgresult_ptr is not None: logging.debug(cur.fetchall())

    return 0

def SQL_get_order(cur, id_order: int) -> tuple[list]:
    cur.execute(f"SELECT * FROM blinov_oboldin.Order WHERE blinov_oboldin.Order.id_order={id_order}")
    if cur.pgresult_ptr is None: return ""

    return cur.fetchall()

def SQL_get_my_orders(cur, id_user: int) -> tuple[list]:
    cur.execute(f"SELECT * FROM blinov_oboldin.Order WHERE blinov_oboldin.Order.id_user={id_user} AND blinov_oboldin.Order.status!='done'")
    if cur.pgresult_ptr is None: return ""

    return cur.fetchall()

def SQL_update_order(cur, model: OrderStatusModel) -> int:
    cur.execute(f"SELECT * FROM blinov_oboldin.Order WHERE blinov_oboldin.Order.id_order={model.id_order} AND blinov_oboldin.Order.id_user={model.id_user}")
    if cur.pgresult_ptr is None: return 1

    line = cur.fetchall()[0]
    curr_id_shift, curr_status = line[2], line[6]

    if model.id_shift is None: model.id_shift = curr_id_shift
    if model.status is None: model.status = curr_status

    cur.execute(f"""UPDATE blinov_oboldin.Order SET
                id_shift={model.id_shift},
                status='{model.status}'""")
    return 0