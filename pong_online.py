from tkinter import *
import numpy as np
from math import *
from random import *
import random
import keyboard

tk = Tk()
cnv=Canvas(tk, width=1600, height=900, bg="grey")
cnv.pack(padx=0, pady=0)

#-------------------------------------------------------------------------------------------------------------------------------------------
#variables initiales


#-------------------------------------------------------------------------------------------------------------------------------------------
#class

class player(object):
    def __init__(self, name):
        self.name = name
        self.x = 800
        self.y = 450
        self.vy = 2
        self.draw = 0

class point(object):
    def __init__(self):
        self.x = 800
        self.y = 450
        self.v = 0
        self.vx = 0
        self.vy = 0
        self.alpha = 0
        self.color = "white"
        self.draw = 0

p1 = player(0)
p2 = player(1)
p1.x = 1500
p2.x = 100

ball = point()

#-------------------------------------------------------------------------------------------------------------------------------------------
#draw

def draw():
    cnv.delete(ALL)
    cnv.delete(p1.draw)
    cnv.delete(p2.draw)
    cnv.delete(ball.draw)
    p1.draw = cnv.create_rectangle(p1.x-10, p1.y-75, p1.x+10, p1.y+75, fill="red")
    p2.draw = cnv.create_rectangle(p2.x-10, p2.y-75, p2.x+10, p2.y+75, fill="blue")
    ball.draw = cnv.create_rectangle(ball.x-20, ball.y-20, ball.x+20, ball.y+20, fill=ball.color)
    
#-------------------------------------------------------------------------------------------------------------------------------------------
#control

def control():
    if keyboard.is_pressed("space"):
        ball.v = 1
        ball.alpha = random.random()*np.pi*2 

    if keyboard.is_pressed("up"):
        p1.y -= p1.vy
    if keyboard.is_pressed("down"):
        p1.y += p1.vy
    
    if keyboard.is_pressed("z"):
        p2.y -= p2.vy
    if keyboard.is_pressed("s"):
        p2.y += p2.vy

#-------------------------------------------------------------------------------------------------------------------------------------------
#brain

def brain():
    ball.vx = ball.v*np.cos(ball.alpha)
    ball.vy = ball.v*np.sin(ball.alpha)
    ball.x += ball.vx
    ball.y += ball.vy

    if(ball.x-20 <= 0 or ball.x+20 >= 1600):
        tk.destroy()

#-------------------------------------------------------------------------------------------------------------------------------------------
#new_checkpoint

def new_checkpoint():
    pass

#-------------------------------------------------------------------------------------------------------------------------------------------
#collision

def collision():
    if(ball.y-20 <= 0 or ball.y+20 >= 900):
        ball.alpha *= -1
        
    if(p1.y-75 <= 0):
        p1.y = 75
        
    if(p1.y+75 >= 900):
        p1.y = 825
        
    if(p2.y-75 <= 0):
        p2.y = 75
        
    if(p2.y+75 >= 900):
        p2.y = 825

    if(ball.x+20 >= p1.x-10 and ball.x-20 <= p1.x+10 and ball.y+20 >= p1.y-75 and ball.y-20 <= p1.y+75):
        ball.alpha = (1-(ball.y-p1.y)/300)*np.pi
        ball.v *= 1.01
        ball.color="red"

    if(ball.x-20 <= p2.x+10 and ball.x+20 >= p2.x-10 and ball.y+20 >= p2.y-75 and ball.y-20 <= p2.y+75):
        ball.alpha = (1-(p2.y-ball.y)/300)*np.pi+np.pi
        ball.v *= 1.01
        ball.color="blue"

#-------------------------------------------------------------------------------------------------------------------------------------------
#main

def main():
    control()
    brain()
    collision()
    draw()
    tk.after(1, main)

#-------------------------------------------------------------------------------------------------------------------------------------------

main()
tk.mainloop()