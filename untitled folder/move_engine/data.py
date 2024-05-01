import Ran.Setup.setup as jk

def data(a,b):
    if b == 1:
        if a == 1:
            return jk.room_1.rid
        if a == 2:
            return jk.room_2.rid
        if a == 3:
            return jk.room_3.rid
    if b == 0:
        if a == "room_1":
            return jk.room_1.exp
        if a == "room_2":
            return jk.room_2.exp
        if a == "room_3":
            return jk.room_3.exp