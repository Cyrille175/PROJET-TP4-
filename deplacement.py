from martypy import Marty
my_marty = Marty("wifi","192.168.0.103")    #Adresse à adapter

def forward() :
    my_marty.stand_straight(move_time = 2000)
    my_marty.walk(num_steps = 8, start_foot = 'auto', turn = 0, step_length = 20, move_time = 1500)

def backward() :
    my_marty.stand_straight(move_time = 2000)
    my_marty.walk(num_steps = 8, start_foot = 'auto', turn = 0, step_length = -20, move_time = 1500)

def turn_right() :
    my_marty.stand_straight(move_time = 2000)
    my_marty.walk(num_steps = 4, start_foot = 'auto', turn = -15, step_length = 0, move_time = 1500)

def turn_left() :
    my_marty.stand_straight(move_time = 2000)
    my_marty.walk(num_steps = 4, start_foot = 'auto', turn = 15, step_length = 0, move_time = 1500)

#Permet de tester les déplacements
"""
forward()
turn_right()
turn_left()
backward()
"""