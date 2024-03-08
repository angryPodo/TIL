from cs1robots import*
import time

#100점

load_world("./worlds/hurdles1.wld")
hubo = Robot()
hubo.set_trace("BLUE")

def turn_right():
    for i in range(3):
        hubo.turn_left()
        
while not hubo.on_beeper():
  if hubo.right_is_clear():
    turn_right()
    hubo.move()
    time.sleep(0.3)
  elif hubo.front_is_clear():
    hubo.move()
    time.sleep(0.3)
  else:
    hubo.turn_left()
    time.sleep(0.3)
    
    
        
        