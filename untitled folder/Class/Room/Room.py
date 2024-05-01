class Room:
    def __init__(self, room_size, height, room_id, txt):
        self.siz = room_size
        self.hei = height
        self.exp = {"s": 0, "w": 0, "e": 0, "n": 0}
        self.rid = room_id
        self.rar = []
        self.txt = txt

    def prin_txt(self):
        with open(self.txt, "r") as f:
            qf = f.read()
            print(qf)

    def mak_rar(self, key):
        self.rar.append(key)

    def da_rar(self, keb):
        self.rar.remove(keb)

    def export(self, mov_1):
        back_exp_mov = 0
        if mov_1 >= int(self.siz):
            back_exp_mov = 1
        return back_exp_mov

    def set_exp(self, key, nom):
        if key in self.exp:
            self.exp[key] = nom




