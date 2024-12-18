import pyglet,classes,random

def draw(root,plants,zombie,projectile,sun,inventory,x0):#взятие изображений из папки
    for i in plants:
        if i.hp>0:
            pyglet.resource.image(f"sprites/{i.type}.png").blit(x0+60*(i.x),60*(i.y-1))
            #pyglet.shapes.Rectangle(x0+60*i.x,60*(i.y-1),60,60,color=(255,255,255)).draw()
            #pyglet.shapes.Rectangle(x0+60*i.x+1,60*(i.y-1)+1,58,60,color=(50,255,30)).draw()

    for i in zombie:
        if i.hp>0:
            pyglet.resource.image(f"sprites/{i.head}.png").blit(x0+60*(i.x+1),60*(i.y-1))
            #pyglet.shapes.Rectangle(x0+60*(i.x+1),60*(i.y-1),30,60,color=(255,255,255)).draw()
            #pyglet.shapes.Rectangle(x0+60*(i.x+1)+1,60*(i.y-1)+1,28,60,color=(255,50,30)).draw()

    for i in projectile:
        pyglet.resource.image(f"sprites/{i.prop}.png").blit(x0+60*(i.x+1),60*(i.y-1))
        #pyglet.shapes.Rectangle(x0+60*(i.x+1),60*(i.y-1)+15,10,30,color=(255,255,255)).draw()
        #pyglet.shapes.Rectangle(x0+60*(i.x+1)+1,60*(i.y-1)+16,8,28,color=(50,50,30)).draw()

    for i in sun:
        pyglet.resource.image(f"sprites/sun.png").blit(x0+60*i.x,60*(i.y-1))
        #pyglet.shapes.Rectangle(x0+60*i.x,60*(i.y-1),10,20,color=(255, 255, 255)).draw()
        #pyglet.shapes.Rectangle(x0+60*i.x+1,60*(i.y-1)+1,8,18,color=(255, 255, 0)).draw()
    n=0

    for i in inventory:
        if i.ticks==i.trigger and classes.inventory.sun>=i.cost:
            pyglet.resource.image(f"sprites/{i.type}_ready.png").blit(40*n, root.height-60)
        else:
            pyglet.resource.image(f"sprites/{i.type}_not_ready.png").blit(40*n, root.height-60)
        n+=1
    pyglet.resource.image(f"sprites/sun.png").blit(40*n, root.height-60)
    pyglet.text.Label(f"{classes.inventory.sun}",x=40*n,y=root.height-60).draw()

def maincycle(root,plants,zombie,projectile,sun,inventory,ticks):
    if ticks%15==0: #частота спавна солнц
        if random.randint(0,3)==3:
            sunspawn()

    if ticks%120==0: #частота спавна зомби
        if random.randint(0,2)==2:
            zombiespawn()

    for i in plants: #действия растений 
        i.live()
        if i.hp<=0:
            next
        i.tick+=1
        if i.tick==i.trigger:
            i.tick=0
            i.function()

    for i in zombie: #действия зомби
        i.live()
        i.collision()
    n=1

    for i in projectile: #анимация снаряда
        i.collision()
        n+=1

    for i in sun: #анимация солнц
        i.ticks+=1
        i.move()

    for i in inventory: #инвентарь
        if i.ticks<i.trigger:
            i.ticks+=1

    root.activate()

def checkings(root,x,y,sun,inventory,x0,chosen): #прибавление солнц и попадание их в инвентарь
    if chosen=="":
        for i in sun:
            if int(x*10) in range(int(i.x*10)*60+x0,x0+100+int(i.x*10)*60):
                if int(y*10) in range(int((i.y-1)*10)*60,int((i.y-1)*10)*60+200):
                    classes.inventory.sun+=25
                    i.ticks=300
                    break
        for i in range(0,len(classes.inventory.allobjects)):
            if x in range(i*40,i*40+40):
                if int(y) in range(root.height-60,root.height):
                    if classes.inventory.allobjects[i].cost<=classes.inventory.sun:
                        if classes.inventory.allobjects[i].ticks==classes.inventory.allobjects[i].trigger:
                            chosen=classes.inventory.allobjects[i]
                            return chosen
        chosen=""
        return chosen
    else:
        xp=(x-x0//10)//60
        if xp<8:
            yp=y//60+1
            if chosen.type!="shovel":
                for i in classes.plants.allobjects:
                    if i.x==xp:
                        if i.y==yp:
                            return ""
                classes.plants(chosen.type,chosen.triggerforplant,chosen.hp,xp,yp)
                classes.inventory.sun-=chosen.cost
                chosen.ticks=0
            else:
                for i in classes.plants.allobjects:
                    if i.x==xp:
                        if i.y==yp:
                            i.hp=0
                            break
        chosen=""
        return chosen

def releaseinventory(): #характеристики инвенторя
    balancefile=open("balance.txt","r")
    balances=balancefile.readlines()
    for i in range(len(balances)):
        if "\n" in balances[i]:
            balances[i]=balances[i][:-1]
    for i in range(len(balances)):
        a=balances[i].split(",")
        classes.inventory(int(a[1]),a[0][1:-1],int(a[2]),int(a[3]),int(a[4]))
    balancefile.close()
    for i in range(1,6):
        classes.plants("lawnmower",1,1,-1,i)

def sunspawn():#отвечает за место спавна солнц
    x=random.randint(0,70)
    y=5
    dy=random.randint(0,50)
    x=x/10
    dy=dy/10
    classes.sun(x,y,dy)

def zombiespawn(): #отвечает за место спавна зомби
    x=9
    y=random.randint(0,5)
    pole=0
    head=random.randint(0,2)
    if head==0:
        pole=random.randint(0,1)
    hp=50+30*head
    speed=0.2+0.2*pole
    classes.zombie(hp,pole,speed,x,y,head)