import classes,pyglet,time,mainmath #запуск
mainmath.releaseinventory()
root=pyglet.window.Window(width=800, height=370, caption='PvZ')
x0=40
tick=time.time()
ticks=0
allandall={}
chosen=""
@root.event

def on_draw(): #сбор всего вместе и запуск
    global tick,x0,ticks
    root.clear()
    mainmath.draw(root,classes.plants.allobjects,
                       classes.zombie.allobjects,
                       classes.projectile.allobjects,
                       classes.sun.allobjects,
                       classes.inventory.allobjects,x0)
    a=time.time()
    if a-tick>=0.3:
        tick=a
        ticks+=1
        mainmath.maincycle(root,classes.plants.allobjects,
                       classes.zombie.allobjects,
                       classes.projectile.allobjects,
                       classes.sun.allobjects,
                       classes.inventory.allobjects,ticks)
@root.event

def on_mouse_press(x, y, button, modifiers):# работа мышки
    global chosen
    chosen=mainmath.checkings(root,x,y,classes.sun.allobjects,classes.inventory,x0*10,chosen)
pyglet.app.run()
#for i in allplants:
#    if i.tick==i.trigger:
#        i.live()
#        i.tick=0
#        i.function()
#for i in allzombies:
#    i.live()
#    i.collision()
#    i.move()
#for i in inventory:
