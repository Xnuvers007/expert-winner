from random import randrange
from turtle import *
from freegames import vector
from tkinter import *
import tkinter.messagebox
import pyfiglet

root = Tk()
tkinter.messagebox.showinfo('ATTENTION...!!!', 'Selamat Datang Di game Canon Ball')
tkinter.messagebox.showinfo('Tutorial', 'CARA BERMAINNYA MUDAH, PENCET MOUSE KIRI UNTUK NEMBAK')
root.mainloop()

root = Tk()
result = tkinter.messagebox.askquestion('Pertanyaan', 'Anda ingin memulai gamenya ?')
if result=='yes':
    theLabel=Label(root, text="Enjoy Gamenya.")
    theLabel.pack()
else:
    root.destroy()
root.mainloop()

print('''

__  __                              __  __      _       _ _  __  __          
\ \/ /_ __  _   ___   _____ _ __ ___\ \/ /_ __ | | ___ (_) |_\ \/ /___ _ __  
 \  /| '_ \| | | \ \ / / _ \ '__/ __|\  /| '_ \| |/ _ \| | __|\  // _ \ '_ \ 
 /  \| | | | |_| |\ V /  __/ |  \__ \/  \| |_) | | (_) | | |_ /  \  __/ | | |
/_/\_\_| |_|\__,_| \_/ \___|_|  |___/_/\_\ .__/|_|\___/|_|\__/_/\_\___|_| |_|
                                         |_|                                 

''')

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respon ketika di tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200
def draw():
    "Gambar Bola dan Target."
    clear()

    for target in targets:
        goto(target.x , target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x , ball.y)
        dot(6, 'red')

    update()
def move():
    "Pergerakan Bola dan Target."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.36
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

root = Tk()
tkinter.messagebox.showinfo('Quit', 'Anda akan Keluar')
root.mainloop(exit())
