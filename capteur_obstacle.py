from martypy import Marty
my_marty = Marty("wifi","192.168.0.116")    #Adresse à adapter

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
        return False
    else :
        return True