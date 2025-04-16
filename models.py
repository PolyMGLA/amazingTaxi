import json

class RegUserModel:
    full_name: str = ""
    phone: str = ""

    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        if len(self.phone) > 0 and self.phone[0] == "8":
            self.phone = "+7" + self.phone[1:]
        for i in range(2, len(self.phone)):
            if i >= len(self.phone): break

            if not self.phone[i].isdigit():
                self.phone = self.phone[:i] + self.phone[i + 1:]

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
    id_user: int = -1
    start_addr: str = ""
    end_addr: str = ""

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
    id_order: int = -1
    id_user: int = -1
    id_shift: int = -1
    # start_addr: str = ""
    # end_addr: str = ""
    # order_time: str = ""
    status: str = ""

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def save(self):
        return json.dumps({
            "id_order": self.id_order,
            "id_user": self.id_user,
            "id_shift": self.id_shift,
            # "start_addr": self.start_addr,
            # "end_addr": self.end_addr,
            # "order_time": self.order_time,
            "status": self.status
             })
    
    @staticmethod
    def load(j: str):
        enc = json.loads(j)
        return OrderStatusModel(**enc)

    @staticmethod
    def load_(data: dict):
        return OrderStatusModel(**data)