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
    mainmath.draw(root,classes.Plants.allobjects,
                       classes.Zombie.allobjects,
                       classes.Projectile.allobjects,
                       classes.Sun.allobjects,
                       classes.Inventory.allobjects,x0)
    a=time.time()
    if a-tick>=0.3:
        tick=a
        ticks+=1
        mainmath.maincycle(root,classes.Plants.allobjects,
                       classes.Zombie.allobjects,
                       classes.Projectile.allobjects,
                       classes.Sun.allobjects,
                       classes.Inventory.allobjects,ticks)
@root.event

def on_mouse_press(x, y, button, modifiers):# работа мышки
    global chosen
    chosen=mainmath.checkings(root,x,y,classes.Sun.allobjects,classes.Inventory,x0*10,chosen)
pyglet.app.run()
