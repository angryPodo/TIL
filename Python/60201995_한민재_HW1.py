from cs1robots import*

#You need to define the size of the map.
n=8 #avenues=n,streets=n
m=n*n
create_world(avenues=n,streets=n)
hubo = Robot(beepers=m)
hubo.set_trace("BLUE")
        
def turn_right():
    for i in range(3):
        hubo.turn_left()        

def move_and_drop():
    if not hubo.on_beeper():
        hubo.drop_beeper()
    hubo.move()

def move_and_drop_to_wall():
    while hubo.front_is_clear():
        move_and_drop()

def drop_and_move():
    if hubo.front_is_clear():
        while not hubo.on_beeper():
            hubo.drop_beeper()
            hubo.move()
    
def start():
    for i in range(4):
        move_and_drop_to_wall()
        hubo.turn_left()
        
def u_turn():
    if hubo.on_beeper():
        hubo.turn_left()
        hubo.turn_left()
        if hubo.front_is_clear():
            hubo.move()
            turn_right()
            if hubo.front_is_clear():
                hubo.move()
    
start()
turn_right()
while hubo.carries_beepers():
    u_turn()
    drop_and_move()