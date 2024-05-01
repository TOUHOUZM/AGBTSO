import Defac.def_ui
import Ran.Setup.setup as jk

def user_li(q1):
    if q1 == "查看房间的信息":
        a = int(jk.user_1.pos)
        if a == 1:
            jk.room_1.prin_txt()
        if a == 2:
            jk.room_2.prin_txt()
        if a == 3:
            jk.room_3.prin_txt()
    if q1 == "打开背包":
        Defac.def_ui.ui("背包")
        print("1 |" + jk.user_1.bag["b1"])
        print("2 |" + jk.user_1.bag["b2"])
        print("3 |" + jk.user_1.bag["b3"])
        print("4 |" + jk.user_1.bag["b4"])
    if q1 == "查看当前状态":
        with open("/Users/liangliang/untitled folder/txt/user.txt", "w") as f:
            f.write("======lif======\n")
            f.write(str(jk.user_1.lif) + "\n")
            f.write("======agg======\n")
            f.write(str(jk.user_1.agg) + "\n")
            f.write("======phy======\n")
            f.write(str(jk.user_1.phy))
            f.write("======pos======\n")
            f.write(str(jk.user_1.pos))
    if q1 == "查看地图":
        with open("/Users/liangliang/untitled folder/txt/map.txt", "r") as f:
            qf = f.read()
            print(qf)
    if q1 == "查看房间状态":
        if int(jk.user_1.pos) == 1:
            Defac.def_ui.ro_ui(jk.room_1)
        if int(jk.user_1.pos) == 2:
            Defac.def_ui.ro_ui(jk.room_2)
        if int(jk.user_1.pos) == 3:
            Defac.def_ui.ro_ui(jk.room_3)
    if q1 == "::help":
        with open("/Users/liangliang/untitled folder/txt/help.txt", "r") as f:
            qf = f.read()
            print(qf)
    if q1 == "查看用户的状态":
        Defac.def_ui.ui("lif")
        print(str(jk.user_1.lif))
        Defac.def_ui.ui("agg")
        print(str(jk.user_1.agg))
        Defac.def_ui.ui("str")
        print(str(jk.user_1.phy))
        Defac.def_ui.ui("pos")
        print(str(jk.user_1.pos))
    if q1 == "查看房间里的物品":
        if int(jk.user_1.pos) == 1:
            Defac.def_ui.ui("房间里的物品")
            qwe = jk.room_1.rar
            for x in qwe:
                print(x)
