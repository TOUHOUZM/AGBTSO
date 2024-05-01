import Ran.play
import Ran.user_li

print('''
制作者：TOUHOU_ZM
 ----=====+基于文本流输出的冒险游戏+=====----
 ''')
print('''
这个程序是开源程序, 遵循MIT协议
1 | ::out  | 退出
2 | ::help | 帮助
3 | ::MIT  | 查看开源协议
        ''')
if __name__ == '__main__':
    q2 = "1"
    while q2 == "1":
        q = input("[host user]$")
        Ran.user_li.user_li(q)
        Ran.play.play(q)
        if q == "::out":
            q2 = ""
