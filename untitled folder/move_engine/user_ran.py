import Ran.Setup.setup as jk

def son_2(a, b):
    qaa = jk.user_1.move()
    if a == "room_1":
        qee = jk.room_1.export(qaa)
    if a == "room_2":
        qee = jk.room_2.export(qaa)
    if a == "room_3":
        qee = jk.room_3.export(qaa)
    if int(qee) == 1:
        jk.user_1.setpos(b)
        return qee


def user_ran(b, s, w, e, n, room, c):
    if b == "向北":
        if n == 1:
            son_2(room, c)
        else:
            print("no way")
    if b == "向西":
        if w == 1:
            son_2(room, c)
        else:
            print("no way")
    if b == "向东":
        if e == 1:
            son_2(room, c)
        else:
            print("no way")
    if b == "向南":
        if s == 1:
            son_2(room, c)
        else:
            print("no way")
