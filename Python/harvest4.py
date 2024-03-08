from cs1robots import*
import time

load_world("./worlds/harvest4.wld")
hubo = Robot()
hubo.set_trace("BLUE")

def turn_right():
    for i in range(3):
        hubo.turn_left()

