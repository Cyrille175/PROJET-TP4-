from capteur_obstacle import obstacle
from martypy import Marty
my_marty = Marty("wifi","192.168.0.100")    #Adresse à adapter

def stand() :
    my_marty.stand_straight(move_time = 2000)

def forward() :
    my_marty.walk(num_steps = 1, start_foot = 'auto', turn = 0, step_length = 20, move_time = 1500)

def backward() :
    my_marty.walk(num_steps = 1, start_foot = 'auto', turn = 0, step_length = -20, move_time = 1500)

def right() :
    my_marty.sidestep(side = 'right', steps = 1, step_length = 20, move_time = 1500)

def left() :
    my_marty.sidestep(side = 'left', steps = 1, step_length = 20, move_time = 1500)

def forward_case() :
    my_marty.walk(num_steps = 8, start_foot = 'auto', turn = 0, step_length = 20, move_time = 1500)

def backward_case() :
    my_marty.walk(num_steps = 8, start_foot = 'auto', turn = 0, step_length = -20, move_time = 1500)

def right_case() :
    my_marty.sidestep(side = 'right', steps = 9, step_length = 20, move_time = 1500)

def left_case() :
    my_marty.sidestep(side = 'left', steps = 9, step_length = 20, move_time = 1500)

#Permet de tester les déplacements
#forward()
#right()
#left()
#backward()
#stand()
#forward_case()
#backward_case()
#right_case()
#left_case()