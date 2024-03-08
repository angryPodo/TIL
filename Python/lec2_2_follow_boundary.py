import time
from cs1robots import*
load_world("./worlds/amazing1.wld")

hubo = Robot(beepers = 1)
hubo.set_trace("red")


def move_or_turn():
  if hubo.front_is_clear():
    hubo.move()
  else:
    hubo.turn_left()

#for i in range(20):
while True:
  move_or_turn()
  time.sleep(0.1)
