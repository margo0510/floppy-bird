import pgzrun 
from random import randint 

TITLE = "FLAPPY BALL"
HEIGHT = 600
WIDTH = 800 

class Ball():
    def __init__(self, initial_x, initial_y):
        self.y = initial_y
        self.x = initial_x
        self.vx = 200
        self.vy = 0 
        self.radius = 40

    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,CLR)


ball = Ball(50,100)

def draw():
    screen.clear()
    ball.draw()


pgzrun.go()
