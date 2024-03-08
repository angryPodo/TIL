from cs1robots import*
import time

create_world(streets=15,avenues=2)
hubo = Robot()
hubo.set_trace("BLUE")

def turn_right():
    for i in range(3):
        hubo.turn_left()
    
def go_straight():
    while hubo.front_is_clear():
        hubo.move()

def zig():
    hubo.move()
    turn_right()
    go_straight()
    hubo.turn_left()
    
def zag():
    hubo.move()
    hubo.turn_left()
    go_straight()
    turn_right()


#start

hubo.turn_left()
go_straight()
turn_right()


while 1:
    zig()
    if not hubo.front_is_clear():
        break
    zag()
    if not hubo.front_is_clear():
        break
        
#end


