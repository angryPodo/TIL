from cs1robots import *
import time
#감점1개

#맵 선택
load_world("./worlds/rain2.wld")

hubo = Robot(beepers=100, avenue=2, street=6,orientation="E")#비퍼 10개여야함,감점1개
hubo.set_trace("BLUE")


def turn_right(robot):
    for i in range(3):
        robot.turn_left()

def follow_left_wall(robot):
    if robot.left_is_clear():
        robot.turn_left()
        robot.move()
        if robot.right_is_clear() and robot.left_is_clear():#창문 판단
            robot.turn_left()
            robot.turn_left()
            robot.drop_beeper()
            robot.move()
            robot.turn_left()
            robot.move()
    elif robot.front_is_clear():
        robot.move()
    else:
        turn_right(robot)

#동작 시작

hubo.drop_beeper()
turn_right(hubo)
hubo.move()
while not hubo.on_beeper():
    follow_left_wall(hubo)
time.sleep(5)
