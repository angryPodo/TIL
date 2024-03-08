from cs1robots import*
import time
#감점 2개

avenue = input("avenue?\n")
street = input("street?\n")
ave_hubo = input("avenue of hubo?\n")
str_hubo = input("street of hubo?\n")
ori_hubo = input("orientaion of hubo?\n")
width = int(avenue)
height = int(street)
aoh = int(ave_hubo)
soh = int(str_hubo)
orih = ori_hubo
create_world(streets=height,avenues=width) #위치바뀜 감점1개

hubo=Robot(avenue=aoh,street=soh,orientation=orih)
hubo.set_trace("BLUE")

def turn_right():
    for i in range(3):
        hubo.turn_left()
        

while not hubo.facing_north():
    hubo.turn_left()
hubo.turn_left()
while hubo.front_is_clear():
    hubo.move()
hubo.turn_left()
hubo.turn_left()
k=0
while hubo.front_is_clear():
    hubo.move()
    k+=1
s=k+1
while hubo.front_is_clear():
    hubo.move()
turn_right()
while hubo.front_is_clear():
    hubo.move()
hubo.turn_left()
hubo.turn_left()
m=0
while hubo.front_is_clear():
    hubo.move()
    m+=1
a=m+1

    
print((s,a))#값이 반대로 됨, 감점1개
    
