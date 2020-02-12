# -*- coding: utf-8 -*-
"""

@author: Brock


Practice Exercises for Mouse and List Methods
https://www.coursera.org/learn/interactive-python-2/supplement/ZbVYV/practice-exercises-for-mouse-and-list-methods-optional
"""


###########################################################3
#1) http://www.codeskulptor.org/#user46_EDlcfhGjA6_0.py
import simplegui

WIDTH = 450
HEIGHT = 600

def click(pos):
    
    print "Mouse click at " +str(pos)
    
frame = simplegui.create_frame("Mouse Click", WIDTH, HEIGHT)
frame.set_canvas_background("White")

frame.set_mouseclick_handler(click)



############################################################
#http://www.codeskulptor.org/#user46_WbWD8xK0EM_0.py

# Circle clicking problem

###################################################
# Student should enter code below

import simplegui
import math

# define global constants
RADIUS = 20
RED_POS = [50, 100]
GREEN_POS = [150, 100]
BLUE_POS = [250, 100]

# define helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define mouseclick handler
def click(pos):
    
    if distance(RED_POS, pos) < RADIUS:
        print "clicked red ball"
    elif distance(GREEN_POS, pos) < RADIUS:
        print "clicked green ball"
    elif distance(BLUE_POS , pos) < RADIUS:
        print "clicked blue ball"
          

# define draw
def draw(canvas):
    canvas.draw_circle(RED_POS, RADIUS, 1, "Red", "Red")
    canvas.draw_circle(GREEN_POS, RADIUS, 1, "Green", "Green")
    canvas.draw_circle(BLUE_POS, RADIUS, 1, "Blue", "Blue")
    
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()



#################################################################
#http://www.codeskulptor.org/#user46_otooyx1Lqu_0.py

# Day to number problem

###################################################
# Student should enter code below

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_to_number2(day):
    return day_list.index(day)

def day_to_number(day):
    pos = 0
    for i in day_list:
        if i == day:
            return pos
        else:
            pos += 1


################################################################3
#http://www.codeskulptor.org/#user46_yvlkIQCWIM_0.py 
            
            # String list joining problem

###################################################
# Student should enter code below

def string_list_join(string_list):
    new_string = ""
    for string in string_list:
        new_string += string
    return new_string


################################################################
#http://www.codeskulptor.org/#user46_mz58cxXpeD_0.py
    
# Ball grid slution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            canvas.draw_circle([2 * BALL_RADIUS * x + BALL_RADIUS,
                                2 * BALL_RADIUS * y + BALL_RADIUS], 
                                BALL_RADIUS, 1, 'Red', 'Red')
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()





################################################################
#http://www.codeskulptor.org/#user46_areSosdOIW_0.py

# Polyline drawing problem

###################################################
# Student should enter code below

import simplegui
import math

polyline = []


# define mouseclick handler
def click(pos):
    polyline.append(pos)
          
# button to clear canvas
def clear():
    global polyline
    polyline = []

# define draw
def draw(canvas):
    if len(polyline) > 0:
        canvas.draw_circle(polyline[0], 1, 1, "White", "White")
        canvas.draw_polyline(polyline, 2, "White")
                    
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()