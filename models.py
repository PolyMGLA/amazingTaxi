import json

class RegUserModel:
    fio = ""
    telephone = ""

    def __init__(self, fio: str, telephone: str):
        self.fio = fio
        self.telephone = telephone

    def save(self):
        return json.dumps({"fio": self.fio, "telephone": self.telephone})
    
    def load(j: str):
        enc = json.loads(j)
        return RegUserModel(enc["fio"], enc["telephone"])
    
class CreateOrderModel:
    id_user = -1
    start_addr = ""
    end_addr = ""

    def __init__(self, id_user: int, start_addr: str, end_addr: str):
        self.id_user = id_user
        self.start_addr = start_addr
        self.end_addr = end_addr

    def save(self):
        return json.dumps({"id_user": self.id_user, "start_addr": self.start_addr, "end_addr": self.end_addr})
    
    def load(j: str):
        enc = json.loads(j)
        return CreateOrderModel(enc["id_user"], enc["start_addr"], enc["end_addr"])