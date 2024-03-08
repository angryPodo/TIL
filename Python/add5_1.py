import time
from cs1robots import*
load_world("./worlds/add34.wld")

hubo = Robot(beepers = 100, avenue=1, street=2)

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()
        
def sense(robot):
    n=0
    while robot.on_beeper():
        robot.pick_beeper()
        n+=1
    return n

def manual_drop(robot,m):
    for _ in range(m):
        robot.drop_beeper()
        
    
def pick_sense_move(robot):
    total=0
    total=total*10+sense(robot)
    while robot.front_is_clear():
        robot.move()
        time.sleep(0.5)
        total=total*10+sense(robot)
    return total

def pick_sense_drop_move(robot,total):
    total+=sense(robot)
    number_drop=total%10
    total=total//10
    manual_drop(robot,number_drop)
    while robot.front_is_clear():
        print(total)
        robot.move()
        time.sleep(0.5)
        total+=sense(robot)
        number_drop=total%10
        total=total//10
        manual_drop(robot,number_drop)
        
total=pick_sense_move(hubo)
turn_right(hubo)
hubo.move()
turn_right(hubo)
pick_sense_drop_move(hubo,total)