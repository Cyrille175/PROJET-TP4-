from martypy import Marty
from connection import my_marty

#Capteur obstacle
obstacle_left = my_marty.foot_obstacle_sensed('left')
obstacle_right = my_marty.foot_obstacle_sensed('right')

if (obstacle_left) : 
    print("Obstacle devant le pied gauche")

if (obstacle_right) : 
    print("Obstacle devant le pied droit")

def obstacle() :
    if (obstacle_right or obstacle_left) :
        print("Mouvement impossible : obstacle détécté")
        return True
    else :
        return False