class Article:
    def __init__(self, item_id, txt, item_name, item_number):
        self.id = item_id
        self.txt = txt
        self.name = item_name
        self.number = item_number

    def prin_txt(self):
        with open(self.txt, "r") as f:
            qf = f.read()
            print(qf)
    def prin_id(self,name1):
        if name1 == "药水":
            return self.id
        else:
            return None

