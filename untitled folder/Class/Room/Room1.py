import Class.Room.Room


class Room1(Class.Room.Room.Room):
    def __init__(self, roo, hei, monster, mons_life, mons_att, rod, ttx):
        super().__init__(room_size=roo, height=hei, room_id=rod, txt=ttx)
        self.mot = monster
        self.mlf = mons_life
        self.mtt = mons_att

    def ro_att(self, att_1):
        if int(att_1) >= int(self.mlf) * int(self.mot):
            back_ro_att = 1
        else:
            back_ro_att = 0
            # 是不是击败了
            back_ro_mot_att = int(self.mtt) * int(self.mot)
            # 受到了多少攻击
        li_back = {"1": back_ro_mot_att, "2": back_ro_att}
        return li_back
    def set_exp(self, key, nom):
        if key in self.exp:
            self.exp[key] = nom