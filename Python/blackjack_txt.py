import random
import time

FACES = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
SUITS = [ "Clubs", "Diamonds", "Hearts", "Spades" ]

class Card():
  def __init__(self,face,suit):
    self.face = face
    self.suit = suit
    
  def __str__(self):
    article = "a "
    if self.face in [8, "Ace"]:
      article = "an "
    return article + str(self.face) + " of " + self.suit

  def value(self):
    if type(self.face) == int:
      return self.face
    if self.face == "Ace":
      return 11
    return 10

class Deck():
  def __init__(self):
    self.cards=[]
    for suit in SUITS:
      for face in FACES:
        card = Card(face,suit)
        self.cards.append(card)
    random.shuffle(self.cards) 

  def draw(self): 
    return self.cards.pop()

def hand_value(someone_hand):
    sum = 0
    for nowValue in someone_hand:
        sum += nowValue.value()
    return sum

def ask_yesno(prompt):
  while True :
    user_input = input(prompt)
    if user_input == "y" :
      return True
    elif user_input == "n" :
      return False
    else :
      print("I beg your pardon!")
  
### (TASK5) 처음에 카드 받는 단계
### palyer 리스트에 deck에서 뽑은 카드를 추가하시오. 추가하면서 어떤 카드가 뽑혔는지 프린트하시오 (예시: "You are dealt a 6 of hearts")
### 그다음으로 카드를 뽑아서 dealer 리스트에 추가하시오. 다만 hidden 카드이므로 딜러가 히든 카드를 뽑았다고 프린트하시오 ("Dealer is dealt a hidden card")
### 그 다음은 다시 palyer 리스트에 deck에서 뽑은 카드를 추가하시오. 추가하면서 어떤 카드가 뽑혔는지 프린트하시오 ("You are dealt a 3 of Spades")
### 그 다음은 dealer 리스트에 deck에서 뽑은 카드를 추가하시오. 추가하면서 어떤 카드가 뽑혔는지 프린트하시오 ("Dealer is dealt a 3 of spades")
### 마지막으로 플레이어의 2장의 카드의 합을 프린트하시오 ("Your total is 9")
  
def blackjack():
  deck = Deck()
  dealer = []
  player = []
  
  player_card1 = deck.draw()
  player.append(player_card1)
  print("-Your are dealt",player_card1,"-")
  time.sleep(1)
  
  dealer_hidden = deck.draw()
  dealer.append(dealer_hidden)
  print("*Dealer is dealt a hidden card*")
  time.sleep(1)
  
  player_card2 = deck.draw()
  player.append(player_card2)
  print("-Your are dealt",player_card2,"-")
  time.sleep(1)
  
  dealercard2 = deck.draw()
  dealer.append(dealercard2)
  print("*Dealer is dealt",dealercard2,"*")
  time.sleep(1)
  print("-Your total is",hand_value(player),"-")
  time.sleep(1)
  
  while(hand_value(player)<21 and ask_yesno("Would you like another card? (y/n)")):
      card3 = deck.draw()
      player.append(card3)
      print("-Your card dealt",card3,"-")
      print("-Your total is ",hand_value(player),"-")
      time.sleep(1)
  print("*The dealers's hidden card was",dealer_hidden,"*")
  time.sleep(1)
  
  ### (TASK7) 21을 넘는지 확인하고, 딜러가 카드를 받는 단계
  ### player 리스트안의 카드들의 합이 21을 넘는지 확인하고 넘었다면 "You went over 21! You lost!"를 프린트하고 -1을 반환하여 함수를 종료합니다.
  ### dealer 리스트 카드들의 합이 17을 넘지 않는다면 계속해서 카드를 추가하고 어떤 카드를 받았는지 출력하세요. ("Dealer is dealt a 5 of spades")
  ### 최종적으로 dealer 리스트 카드 합의 값을 프린트하세요. ("The dealer's total is 18")
  
  if(hand_value(player)>21):
    print("You went over 21! You lost!")
    return -1
  else:
    while(hand_value(dealer)<17):
      dealercard3 = deck.draw()
      dealer.append(dealercard3)
      print("*Dealer is dealt",dealercard3,"*")
      time.sleep(1)
  
  print("-Your total is ",hand_value(player),"-")
  print("*The dealer's total is",hand_value(dealer),"*")
  if(hand_value(dealer)>21):
    print("Dealer went over 21! You win! :)")
    time.sleep(1)
    return -1
  elif(hand_value(player)>hand_value(dealer)):
    print("You win! :)")
    time.sleep(1)
  elif(hand_value(player)==hand_value(dealer)):
    print("You have a tie :|")
    time.sleep(1)
  else:
    print("You lose :/")
    time.sleep(1)
    
def game_loop():
  print("***Welcome to Blackjack!***")   
  while True:
    blackjack()    
    if not ask_yesno("***Play another round? (y/n)***"):
      break    

game_loop()
