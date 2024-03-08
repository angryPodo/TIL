import time
from cs1robots import*

create_world()

hubo=Robot( orientation= "N" , beepers = 0, avenue= 10, street = 1)
hubo.set_trace("red")


print
def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()
  
def turn_around():
  hubo.turn_left()
  hubo.turn_left()
  
def move_nine():
    for i in range(9):
        hubo.move()
        time.sleep(0.1)
        
def one_sequence():
  for i in range(4):
    move_nine()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    move_nine()
    turn_right()
    hubo.move()
    turn_right()


one_sequence()
move_nine()
hubo.turn_left()
hubo.move()
hubo.turn_left()
move_nine()





