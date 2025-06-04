import time
from martypy import Marty

MARTY_IP = "192.168.0.107"  # Update this if the IP changes

# Connect to Marty
try:
    marty = Marty("wifi", MARTY_IP)
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

#  Eye expression functions

def eyes_normal():
   
    marty.eyes("normal")
    print("Normal eyes")
    time.sleep(2)

def eyes_angry():
   
    marty.eyes("angry")
    print("Angry eyes")
    time.sleep(2)

def eyes_excited():
   
    marty.eyes("excited")
    print("Excited eyes")
    time.sleep(2)

def eyes_wide():
    
    marty.eyes("wide")
    print("Wide open eyes")
    time.sleep(2)

def eyes_wiggle():
    
    marty.eyes("wiggle")
    print("Wiggling eyes")
    time.sleep(2)
    
    
eyes_wiggle()