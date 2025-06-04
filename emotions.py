import time
from martypy import Marty

MARTY_IP = "192.168.0.107"  # Update this if the IP changes

# Connect to Marty
marty = Marty("wifi", MARTY_IP)


#  Eye expression functions

def eyes_normal():
    
    marty.eyes("normal")
    print("Normal eyes")
    marty.disco_color("green")
    time.sleep(2)

def eyes_angry():
    marty.disco_color("red")
    marty.eyes("angry")
    print("Angry eyes")
    time.sleep(2)

def eyes_excited():
   
    marty.disco_color("blue")
    marty.eyes("excited")
    print("Excited eyes")
    time.sleep(2)

def eyes_wide():
    marty.disco_color("green")
    marty.eyes("wide")
    print("Wide open eyes")
    
    for i in range(4):
        marty.disco_color("blue")
        print("set to blue")
        time.sleep(0.4)
        marty.disco_color("green")
        print("set to green")
        time.sleep(0.2)
        
    marty.disco_color("green")
    
def eyes_wiggle():
    
    marty.eyes("wiggle")
    print("Wiggling eyes")
    time.sleep(2)
    
def applyEmotion(emotionName):
    if emotionName == "normal":
        eyes_normal()
    elif emotionName == "angry":
        eyes_angry()
    elif emotionName == "excited":
        eyes_excited()
    elif emotionName == "wide":
        eyes_wide()
    elif emotionName == "wiggle":
        eyes_wiggle()

