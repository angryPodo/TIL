from cs1graphics import *
from time import *
import random

canvas = Canvas(640, 580)
canvas.setTitle("Memento")

path = "/Users/mr_han/TIL/Python/images/"
names = ("pika.png", "firi.PNG", "green.PNG", "othergreen.PNG", "liza.PNG", "strange.PNG")

cards = []  
num_pads = []  
correct_list = []  

def initialize():
    for i in range(6):
        for k in range(4):
            img = Image(path + names[i])
            temp_tuple = (img, names[i])
            cards.append(temp_tuple)

    for i in range(24):
        card = Layer()
        rect = Rectangle(90, 120, Point(0, 0))
        text = Text(str(i), 18, Point(0, 0))
        card.add(rect)
        card.add(text)
        num_pads.append(card)
        
    random.shuffle(cards)

def print_cards():
    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range(len(num_pads)):
        if i in correct_list:
            cards[i][0].moveTo(i_w + w, i_h + h)
            canvas.add(cards[i][0])
        else:
            num_pads[i].moveTo(i_w + w, i_h + h)
            canvas.add(num_pads[i])

        w += 100
        if w % 600 == 0:
            w = 0
            h += 130
#TASK1
def is_valid(num1, num2):
    if num1 in range(24) and num2 in range(24):
        if num1 != num2:
            if num1 not in correct_list and num2 not in correct_list:
                return True
    return False
#TASK2
def check(num1, num2):
    correct_list.append(num1)
    correct_list.append(num2)
    print_cards()
    if cards[num1][1]!=cards[num2][1]: 
        sleep(1)
        correct_list.remove(num1)
        correct_list.remove(num2)
        print_cards()
        print("Wrong!")
        return False
    else:
        print("Correct!")
        return True
#카드게임 시작
initialize()
#TAST3
for i in range(24):
    correct_list.append(i)
print_cards()
sleep(10)
for i in range(24):
    correct_list.remove(i)
print_cards()
#TASK4
print("### Welcome to the Python Memento game!!! ###")
tries=1
while len(correct_list) < 24:
    print("%d-th try" %tries)
    print("You got %d pairs" %int(len(correct_list)/2))
    
    num1 = int(input("Input the first card number: "))
    num2 = int(input("Input the second card number: "))
    
    if is_valid(num1,num2):
        tries+=1
        check(num1,num2)
    else:
        tries+=1
            
print("End of memento")
#게임 끝!!!