from martypy import Marty


my_marty = Marty("wifi", "192.168.0.103")
battery = my_marty.get_battery_remaining()
print(battery)

#Ceci me renvoie le niveau de batterie en pourcentage