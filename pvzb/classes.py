class Zombie: #характеристики зомби
    allobjects=[]
    def __init__(self,hp,pole,speed,x,y,head):
        self.hp=hp
        self.pole=pole
        self.speed=speed
        self.x=x
        self.y=y
        self.head=head
        Zombie.allobjects.append(self)
    def collision(self):#зомби ходьба
        domove=1
        for i in Plants.allobjects:
            if i.y==self.y:
                if int(i.x*10) in range(int(self.x*10-self.speed*10),int(self.x*10)+1):
                    domove=0
                    if self.x!=i.x:
                        self.x=i.x
                        break
                    if self.pole:
                        self.x+=1
                        self.pole=0
                    else:
                        i.hp-=10
        if domove:
            self.x-=self.speed
            self.x=round(self.x,2)
    def live(self): #смерть зомби
        if self.hp<=0:
            del Zombie.allobjects[Zombie.allobjects.index(self)]
            del self

class Plants: #характеристики растегий
    allobjects=[]
    def __init__(self,type,trigger,hp,x,y):
        self.type=type
        self.trigger=trigger
        self.hp=hp
        self.tick=0
        self.x=x
        self.y=y
        Plants.allobjects.append(self)

    def function(self):#способность растения
        match self.type:
            case "cherrybomb":
                for i in Zombie.allobjects:
                    if i.y==self.y:
                        if int(i.x*10) in range(int((self.x-1)*10),int((self.x+1)*10)):
                            i.hp=0
                self.hp=0
            case "chomper":
                if self.trigger==320:
                    self.trigger=1
                for i in Zombie.allobjects:
                    if i.y==self.y:
                        if int(i.x*10) in range(int((self.x)*10),int((self.x+1)*10)):
                            i.hp=0
                            self.trigger=320
                            break
            case "Sunflower":
                Sun(self.x+0.2,self.y,self.y)
            case "peashooter":
                mindistant=9
                mini=""
                for i in Zombie.allobjects:
                    if i.y==self.y:
                        Projectile(0.4,20,"",self.x,self.y)
                        break
            case "repeater":
                mindistant=9
                mini=""
                for i in Zombie.allobjects:
                    if i.y==self.y:
                        Projectile(0.4,20,"",self.x,self.y)
                        Projectile(0.4,20,"",self.x,self.y)
                        break
            case "snow_peashooter":
                mindistant=9
                mini=""
                for i in Zombie.allobjects:
                    if i.y==self.y:
                        Projectile(0.4,20,"ice",self.x,self.y)
                        break
            case "wallnut":
                pass
            case "lawnmower":
                trig=0
                for i in Zombie.allobjects:
                    if i.y==self.y:
                        if i.x==self.x:
                            trig=1
                if trig:
                    self.hp=0
                    for i in Zombie.allobjects:
                        if i.y==self.y:
                            i.hp=0
            case "potatomine":
                self.trigger=1
                for i in Zombie.allobjects:
                    if i.y==self.y:
                        if i.x==self.x:
                            i.hp=0
                            self.hp=0
                            break

    def live(self):#смерть растения
        if self.hp<=0:
            del Plants.allobjects[Plants.allobjects.index(self)]
            del self

class Inventory:# характеристики инвенторя
    Sun=50
    allobjects=[]
    def __init__(self,trigger,type,triggerp,hp,cost):
        self.ticks=0
        self.trigger=trigger
        self.type=type
        self.triggerforplant=triggerp
        self.hp=hp
        self.cost=cost
        Inventory.allobjects.append(self)

class Sun:# хаоактеристики солнц
    allobjects=[]
    def __init__(self,x,y,dy):
        self.x=x
        self.y=y
        self.dy=dy
        self.trigger=300
        self.ticks=0
        Sun.allobjects.append(self)

    def move(self): #движение солнц
        if self.y>self.dy:
            self.y-=0.2
        if self.ticks>=self.trigger:
            del Sun.allobjects[Sun.allobjects.index(self)]
            del self

class Projectile: # характеристика пуль
    allobjects=[]
    def __init__(self,speed,dmg,prop,x,y):
        self.speed=speed
        self.dmg=dmg
        self.prop=prop
        self.x=x
        self.y=y
        Projectile.allobjects.append(self)

    def collision(self): # взаимодействие пули с зомби
        domove=1
        for i in Zombie.allobjects:
            if i.y==self.y:
                if int(i.x*10) in range(int((self.x-self.speed)*10),int((self.x+self.speed)*10)):
                    domove=0
                    match self.prop:
                        case "ice":
                            i.speed=i.speed/2
                    i.hp-=10
                    del Projectile.allobjects[Projectile.allobjects.index(self)]
                    del self
                    return 0
        if domove:
            self.x+=self.speed
            self.x=round(self.x,2)
        if self.x>9:
            del Projectile.allobjects[Projectile.allobjects.index(self)]
            del self
