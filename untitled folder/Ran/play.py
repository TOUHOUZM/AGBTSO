import Ran.Setup.setup as jk
import Defac.def_ui
import move_engine.user_ran
import move_engine.data
import move_engine.move_ran


def play(b):
    a = int(jk.user_1.pos)
    ugg = move_engine.data.data(a, 1)
    bb = jk.user_1.pos
    a = move_engine.data.data(bb, 1)
    c = move_engine.data.data(a, 0)
    # 进行移动的处理
    if b == "把物品装入背包":
        if a == 0:
            print("这里什么也没有")
        if a == 1:
            Defac.def_ui.ui("当前物品列表")
            na = input("[sys- user]$")
            na = int(na)
            ca = jk.room_1.rar[na]
            jk.room_1.rar.remove(jk.room_1.rar[na])
            Defac.def_ui.ui("需要输入的物品")
            ad = input("[sys- user]$")
            jk.user_1.makbag(ad, ca)
    if b == "把物品从背包中拿出":
        if a == 0:
            print("这里不可以取出物品")
        if a == 1:
            Defac.def_ui.ui("需要取出的物品")
            ad = input("[sys- user]$")
            na = jk.user_1.bag[ad]
            jk.user_1.dabag(ad)
            jk.room_1.mak_rar(na)
    if b == "查看物品信息":
        Defac.def_ui.ui("需要查看什么物品？")
        ad = input("[sys- user]$")
        if ad == "药水":
            jk.article_1.prin_txt()
    if b == "使用物品":
        Defac.def_ui.ui("何处？")
        ad = input("[sys- user]$")
        m = jk.user_1.bag[ad]
        Defac.def_ui.ui("何物?")
        cd = input("[sys- user]$")
        if cd == "药水":
            if m == "药水":
                a = jk.article_1.ag
                jk.user_1.makeagg(a)
                jk.user_1.dabag(ad)
                print("成功")
            else:
                print("失败")
    if b == "::MIT":
        with open("/Users/liangliang/untitled folder/LICENSE", "r") as f:
            qf = f.read()
            print(qf)

    if b == "移动":
        Defac.def_ui.ui("向哪个方向？")
        ad = input("[sys- user]$")
        move_engine.user_ran.user_ran(ad, move_engine.move_ran.move_ran(c, 1), move_engine.move_ran.move_ran(c, 2),
                                      move_engine.move_ran.move_ran(c, 3), move_engine.move_ran.move_ran(c, 4), ugg, 1)
