  # -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:28:02 2020

@author: Paweł Bąk
"""

import turtle
import random
import time

# Box with boucing balls with theirs sizes, mass and gravity

# Screen settings
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Ball in the box")
wn.tracer(0, 0)

# Classes
class Box(turtle.Turtle):
    """ Class that creates and customize the boundary box"""
    def __init__(self, dye):
        """Set left bottom corner of the box and color"""
        turtle.Turtle.__init__(self)
        self.goto(-400,-400)
        self.color(dye)
        
    def create(self, a):
        """ Creates the box. Variable "a" is a side length of the box"""
        for b in range(4):
            self.forward(a)
            self.left(90)
        self.hideturtle()
            
            
class Ball(turtle.Turtle):
    """ Creates ball object with size (connected to mass), color, appear position and velocities"""
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        
        colors = ["red", "blue", "yellow", "orange", "green", "purple"]
        self.color(random.choice(colors))
        
    def mass(self, mass):
        """Size of ball is connetced with mass. Trutlesize 1 has 20 pixels diameter, diameter value = mass"""
        self.mass = mass
        self.radius = self.mass/2
        
    def position(self, x, y):
        """Appear position inside the box"""
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
    
    def velocity(self, dx, dy):   
        """Vertical and horizontal velocity. dx and dy means how many pixels ball can move in one loop step"""
        self.dx = dx
        self.dy = dy


class CollisionManager(object):
    """Check for collisions between the balls"""    
            
    def collision_without_mass(self):
        """Elastic collision without energy loss and mass
           The balls are swapping velocities when the have contact"""
        for i in range(0, len(balls)):
            for j in range(i+1, len(balls)):
                """Check for a collision"""
                if balls[i].distance(balls[j]) < balls[i].radius + balls[j].radius:
                    balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                    balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy                                      
        
    def collision_with_mass(self):
        """Elastic collision with mass, calculated from law of momentum conservation and kinetic enegry"""
        for i in range(0, len(balls)):
            for j in range(i+1, len(balls)):
                """Check for a collision and find new velocities """
                if balls[i].distance(balls[j]) < balls[i].radius + balls[j].radius:
                    new_i_x = ((balls[i].mass * balls[i].dx + balls[j].mass * balls[j].dx + 
                            balls[j].mass * cor *(balls[j].dx - balls[i].dx))/(balls[i].mass + balls[j].mass))
                    new_j_x = ((balls[i].mass * balls[i].dx + balls[j].mass * balls[j].dx + 
                            balls[i].mass * cor *(balls[i].dx - balls[j].dx))/(balls[i].mass + balls[j].mass))
                    new_i_y = ((balls[i].mass * balls[i].dy + balls[j].mass * balls[j].dy + 
                            balls[j].mass * cor *(balls[j].dy - balls[i].dy))/(balls[i].mass + balls[j].mass))
                    new_j_y = ((balls[i].mass * balls[i].dy + balls[j].mass * balls[j].dy + 
                            balls[i].mass * cor *(balls[i].dy - balls[j].dy))/(balls[i].mass + balls[j].mass))
                    balls[i].dx = new_i_x
                    balls[j].dx = new_j_x
                    balls[i].dy = new_i_y
                    balls[j].dy = new_j_y    
    
    
    
# Creating boundary box
box = Box("red")
box.create(800)

# Creating balls
balls = []

for objects in range(10):
    balls.append(Ball())

# Range for balls appear position, it will be generated randomly

pos = range(-300,300,30) 

# Balls properties
for ball in balls:  
    ball.position(random.choice(pos), random.choice(pos))
    ball.velocity(random.randint(-1, 1), 2)
    ball.mass(random.randint(10,60))
    ball.turtlesize(ball.mass/20)

# Gravity value = 0.02 pixels will be substructed from veritcal velocity each loop step
# Check gravity = 0, it's fun!
gravity = 0

# Stickness coefficent. cor = 1 for elastic collision
cor = 1

# Main loop
while True:
    wn.update()
    time.sleep(0.002)
    for ball in balls:
        
        # Basic movement
        ball.dy -= gravity
        ball.sety(ball.ycor()+ ball.dy)
        
        ball.setx(ball.xcor() + ball.dx)
        
        # Check for contact y with boundary box
        if ball.ycor() < -400 + ball.radius:
            ball.dy *= -1 
            
        if ball.ycor() > 400 - ball.radius:
            ball.dy *= -1
            
        # Check for contact x with boundary box
        if ball.xcor() > 400 - ball.radius:
            ball.dx *= -1
            
        if ball.xcor() < -400 + ball.radius:
            ball.dx *= -1

    """Check for collisions between the balls"""
    """Avaliable = collision without mass, collision with mass"""
    cm = CollisionManager()
    cm.collision_with_mass()
                
wn.mainloop()
