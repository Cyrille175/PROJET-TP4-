from martypy import Marty
my_marty = Marty("wifi","192.168.0.107")    #Adresse à adapter

def forward() :
    my_marty.stand_straight(move_time = 2000)
    my_marty.walk(num_steps = 1, start_foot = 'auto', turn = 0, step_length = 20, move_time = 1500)

def backward() :
    my_marty.stand_straight(move_time = 2000)
    my_marty.walk(num_steps = 1, start_foot = 'auto', turn = 0, step_length = -20, move_time = 1500)

def right() :
    my_marty.stand_straight(move_time = 2000)
    my_marty.sidestep(side = right, steps = 1, step_length = 20, move_time = 1500)

def left() :
    my_marty.stand_straight(move_time = 2000)
    my_marty.sidestep(side = left, steps = 1, step_length = 20, move_time = 1500)

#Permet de tester les déplacements
#forward()
#right()
#left()
#backward()