class Card():
  def __init__(self,face,suit):
    self.face = face
    self.suit = suit
    
firstCard = Card("ugly","ACE")
print(firstCard.suit,'\n')
firstCard.face = 'ham'
firstCard.suit = 'ham'
print(firstCard.suit)