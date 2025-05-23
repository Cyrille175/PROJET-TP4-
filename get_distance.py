
from martypy import Marty


my_marty = Marty("wifi", "192.168.0.103")
distance_sensor1 = my_marty.get_distance_sensor()
n=5
for i in range (n):
    my_marty.walk()
    i= i+1
distance_sensor2 = my_marty.get_distance_sensor()
print(distance_sensor1)
print(distance_sensor2)