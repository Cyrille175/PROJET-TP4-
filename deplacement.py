#from capteur_obstacle import obstacle
from tkinter import *
from martypy import Marty
from connection import my_marty

def stand() :
    my_marty.stand_straight(move_time = 2000)

#Déplacements d'1 pas
def forward() :
    my_marty.walk(num_steps = 1, start_foot = 'auto', turn = 0, step_length = 20, move_time = 1500)

def backward() :
    my_marty.walk(num_steps = 1, start_foot = 'auto', turn = 0, step_length = -20, move_time = 1500)

def right() :
    my_marty.sidestep(side = 'right', steps = 1, step_length = 20, move_time = 1500)

def left() :
    my_marty.sidestep(side = 'left', steps = 1, step_length = 20, move_time = 1500)

#Déplacement d'1 case
def forward_case() :
    my_marty.walk(num_steps = 8, start_foot = 'auto', turn = 0, step_length = 20, move_time = 1500)

def backward_case() :
    my_marty.walk(num_steps = 8, start_foot = 'auto', turn = 0, step_length = -20, move_time = 1500)

def right_case() :
    my_marty.sidestep(side = 'right', steps = 11, step_length = 20, move_time = 1500)

def left_case() :
    my_marty.sidestep(side = 'left', steps = 11, step_length = 20, move_time = 1500)

fen = Tk()

def press_up(event) :
    forward()

def press_down(event) :
    backward()

def press_right(event) :
    right()

def press_left(event) :
    left()

#Déplacements avec les flèches du clavier
fen.bind_all('<Up>', press_up)
fen.bind_all('<Down>', press_down)
fen.bind_all('<Right>', press_right)
fen.bind_all('<Left>', press_left)

fen.mainloop()
#Permet de tester les déplacements
#forward()
#right()
#left()
#backward()
#forward_case()
#backward_case()
#right_case()
#left_case()
stand()