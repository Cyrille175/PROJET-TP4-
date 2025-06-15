import time
from martypy import Marty
from connection import my_marty



#  Eye expression functions

def eyes_normal():
    my_marty.eyes("normal")
    print("Normal eyes")
    my_marty.disco_color("green")


def eyes_angry():
    my_marty.disco_color("red")
    my_marty.eyes("angry")
    print("Angry eyes")


def eyes_excited():
    my_marty.disco_color("blue")
    my_marty.eyes("excited")
    print("Excited eyes")


def eyes_wide():
    my_marty.disco_color("green")
    my_marty.eyes("wide")
    print("Wide open eyes")

    for i in range(4):
        my_marty.disco_color("blue")
        print("set to blue")
        time.sleep(0.4)
        my_marty.disco_color("green")
        print("set to green")
        time.sleep(0.2)

    my_marty.disco_color("green")


def eyes_wiggle():
    my_marty.eyes("wiggle")
    print("Wiggling eyes")


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
