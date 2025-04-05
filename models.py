import json
import logging

class RegUserModel:
    full_name = ""
    phone = ""

    def __init__(self, full_name: str, phone: str):
        self.full_name = full_name
        self.phone = phone

    def save(self):
        return json.dumps({ "full_name": self.full_name, "phone": self.phone })
    
    @staticmethod
    def load(j: str):
        enc = json.loads(j)
        return RegUserModel(**enc)
    
    @staticmethod
    def load_(data: dict):
        return RegUserModel(**data)
    
class CreateOrderModel:
    id_user = -1
    start_addr = ""
    end_addr = ""

    def __init__(self, id_user: int, start_addr: str, end_addr: str):
        self.id_user = id_user
        self.start_addr = start_addr
        self.end_addr = end_addr

    def save(self):
        return json.dumps({ "id_user": self.id_user, "start_addr": self.start_addr, "end_addr": self.end_addr })
    
    @staticmethod
    def load(j: str):
        enc = json.loads(j)
        return CreateOrderModel(**enc)

    @staticmethod
    def load_(data: dict):
        return CreateOrderModel(**data)
    
class OrderStatusModel:
    id_order = -1
    id_user = -1
    id_shift = -1
    start_addr = ""
    end_addr = ""
    order_time = ""
    status = ""

    def __init__(self, order_id: int):
        self.order_id = order_id

    def save(self):
        return json.dumps({
            "id_order": self.id_order,
            "id_user": self.id_user,
            "id_shift": self.id_shift,
            "start_addr": self.start_addr,
            "end_addr": self.end_addr,
            "order_time": self.order_time,
            "status": self.status
             })
    
    @staticmethod
    def load(j: str):
        enc = json.loads(j)
        return CreateOrderModel(**enc)

    @staticmethod
    def load_(data: dict):
        return CreateOrderModel(**data)