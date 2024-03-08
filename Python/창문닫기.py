from cs1robots import *
import time #너무빠르면 타임.슬립으로 느리게 보세요

#맵 선택
load_world("./worlds/rain1.wld")

hubo = Robot(beepers=10, avenue=2, street=6 ,orientation='E')
hubo.set_trace("BLUE")

def turn_right(robot):
    for i in range(3):
        robot.turn_left()
        
def check_window(robot):
    if robot.right_is_clear() and robot.left_is_clear():#양쪽 벽이 뚫렸을때 
            turn_right(robot)
            turn_right(robot)
            robot.move()#제자리로 돌아감
            turn_right(robot)#E방향으로 전환
            robot.drop_beeper()#창문닫기
            robot.move()#전진

def follow_right_wall(robot):
    if robot.right_is_clear():#오른쪽이 비었을때=창문일때
        turn_right(robot)
        robot.move()#창문 밖으로 나감
        check_window(robot)#창문 확인
    elif robot.front_is_clear():
        robot.move()
    else:
        robot.turn_left()

#동작 시작
if hubo.front_is_clear(): #앞이 막혔을때 대비
    hubo.move()
    turn_right(hubo)
    hubo.drop_beeper()#시작과끝위한비퍼
    if hubo.front_is_clear():       
        hubo.move()#while실행위해 비퍼 벗어나기
            
while not hubo.on_beeper():
    follow_right_wall(hubo)