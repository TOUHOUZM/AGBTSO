class UsClass:
    def __init__(self ,life,physical_strength,aggressivity,position):
        self.lif = life
        self.phy = physical_strength
        self.agg = aggressivity
        self.pos = position
        self.bag = {"b1":"","b2":"","b3":"","b4":""}

    def makeagg(self,ag):
        self.agg = int(self.agg) + int(ag)
    def makbag(self,key_bag,article):
        self.bag[key_bag] = article
    def dabag(self,keb):
        self.bag[keb] = ""
    def attack(self):
        a = int(self.phy)/2
        self.agg = int(self.agg)-int(self.phy)
        return a
    def injured(self,d_att):
        self.lif = int(self.lif) + int(d_att)
    def setpos(self,net):
        self.pos = int(self.pos) + net
    def imsetpos(self,net1):
        self.pos = int(self.pos) - net1
    def move(self):
        mov = int(self.agg)/2
        self.agg = int(self.agg) - int(self.agg)/4 - 10
        return mov
