import json

class RegUserModel:
    full_name = ""
    phone = ""

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

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

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

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

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

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
        return OrderStatusModel(**enc)

    @staticmethod
    def load_(data: dict):
        return OrderStatusModel(**data)