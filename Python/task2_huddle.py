import time
from cs1robots import*

load_world("./worlds/hurdles1.wld")

hubo=Robot()
hubo.set_trace("blue")

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def jump_h():
    for i in range(4):
        hubo.move()
        hubo.turn_left()
        hubo.move()
        turn_right()
        hubo.move()
        turn_right()
        hubo.move()
        hubo.turn_left()    
        time.sleep(0.5)

jump_h()
hubo.move()
hubo.pick_beeper()
