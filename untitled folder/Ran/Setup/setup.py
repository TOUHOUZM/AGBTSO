import Class.Room.Room1
import Class.Room.Room
import Class.User.UsClass
import Class.Item.Article

article_1 = Class.Item.Article.Article(1, "/Users/liangliang/untitled folder/txt/item/ys_ar", "药水", 10)

user_1 = Class.User.UsClass.UsClass(100, 90, 80, 1)

room_2 = Class.Room.Room1.Room1(20, 5, 5, 50, 20, "room_2", "/Users/liangliang/untitled folder/txt/room/room3")

room_1 = Class.Room.Room.Room(20, 5, "room_1", "/Users/liangliang/untitled folder/txt/room/room1")
room_3 = Class.Room.Room.Room(20, 5, "room_3", "/Users/liangliang/untitled folder/txt/room/room2")
room_4 = Class.Room.Room.Room(20, 5, "room_4", "/Users/liangliang/untitled folder/txt/room/room4")

room_1.set_exp("n", 1)

room_2.set_exp("w", 1)
room_2.set_exp("n", 1)

room_3.set_exp("n", 1)

room_4.set_exp("n", 1)
room_4.set_exp("e", 1)

room_1.mak_rar(article_1.id)
