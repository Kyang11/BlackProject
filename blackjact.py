from distutils.command.build import build
import os
import random
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class CardTable():
    def __init__(self, value, suit):
        self. suit = suit
        self.value = value
    def show(self):
        print(f"{self.value} of {self.suit}".format(self.value, self.suit))
        
    player_call = True
    dealer_call =True 
    
class Deck(CardTable):
    def __init__(self):
        self.cards=[]
        self.build()
        
    def build(self):
        for s in ["Space", "Clubs", "Diamonds", "Hearts"]:
            
            card_deck=['2','3','4','5','6','7','8','9','10','A','J','Q','K']
            
            for v in card_deck:
                self.cards.append(CardTable(v, s))
                
    def show(self):
        for c in self.cards:
            c.show()
            
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def drawCard(self):
       return self.cards.pop()
   
    def total(self,turn):
        self.total =0
        face=['A','J','Q','K']
        for card in turn:
            if card in range(build.card_deck):
                self.total+=card
            elif card in face:
                self.total+=10
            else:
                if self.total >11:
                    self.total+=1
                else: 
                    self.total+=11
        return self.total
          
class Dealer(CardTable):
    def __init__(self,name):
        self.name =name
        self.dealer_hand=[]
    
    def draw(self, deck): # passing the deck player draw a card from 
        self.deal_hand.append(deck.drawCard())
        return self
    
    def showhand(self):
        for card in self.hand:
            card.show()
    
    def discard(self):
        return self.hand.pop() 
    
     
    def dealercall(self):
          
        self.dealerhand=[] 
        if len(self.dealerhand) != 2:
            self.dealerhand.append(random.randint(build.card_deck))
            return self.dealerhand[0]
        elif len(self.dealerhand) == 2:
            return self.dealerhand[0], self.dealerhand[1] 
    
                  
        while self.dealer_call:
            print(f"Dealer has {self.dealercall()} and X")
            if self.total.dealerhand > 16:
                self.dealer_call= False
            elif self.total.dealerhand < 16:
                self.dealer_hand.append(random.randint(build.card_deck))
                print(f"Dealer has the total of {str(sum(self.dealerhand))} from these card {self.dealerhand}")
            else:
                self.total.dealerhand
                   
class Player(CardTable):
    def __init__(self,name):
        self.name =name
        self.player_hand=[]
    
    def draw(self, deck): # passing the deck player draw a card from 
        self.player_hand.append(deck.drawCard())
        return self
    
    def showhand(self):
        for card in self.player_hand:
            card.show()
    
    def discard(self):
        return self.player_hand.pop()
    
    def play(self):
         
        if len(self.player_hand) !=2:
            self.player_hand.append(random.randint(build.card_deck)) 
            return self.player_hand
        
        elif len(self.player_hand)==2:
                return ("You have", self.player_hand)
                
        while self.player_call:

            if self.total(self.player_hand) < 21:
                decision_making =str(input(f"\n You want to stay or hit?\n Enter 1 for Hit: \n Enter 2 Stay: "))
                
            if decision_making =='1':
                self.player_hand.append(random.randint(build.card_deck))
                
                print(f"You now have the total of {str(sum(self.player_hand))} from these card {self.player_hand}")
                
            elif self.player_hand >21:
    
                print(f"You have a total of {str(sum(self.player_hand))} wiht {self.player_hand} \n")
                print(f"Are you Busted, Dealer Win! :( \n")
                print(f"Dealer has total {str(sum(self.dealerhand))} with {self.dealer_hand}")

                
class compare_dealer_and_player_score(CardTable):
    def __init__(self, dealer_hand, player_hand): 
        self.dealer_hand = dealer_hand
        self.player_hand = player_hand

        while self.dealer_call and self.player_call:
            if self.total.dealer_hand ==21:
                print("Dealer Win!")
                break
            elif self.total.player_hand ==21:
                print("You win!")
            elif self.dealer_hand >21:
                print(f"You has {self.dealer_hand} for total of {self.total.dealer_hand} and dealer has {self.player_hand} out of {self.total.player_hand}\n")
                print(f"Dealer bust! You Win")
            elif self.total.player_hand >21:
                
                print(f"You has {self.playerhand} for total of {self.total.player_hand} and dealer has {self.dealer_hand} out of {self.total.dealer_hand}\n")
                print(f"You bust! dealder Win")  
                        
            elif self.total.player_hand > self.total.dealer_hand:
                print(f" You have {self.player_hand} for total of {self.total.player_hand} and \n  user has {self.dealer_hand} for total of {self.total.dealer_hand} ")
            
            elif self.total.dealer_hand > self.total.player_hand:
                print(f"Dealer has {self.dealer_hand} for total of {self.total.dealer_hand} and dealer has {self.player_hand} out of {self.total.player_hand}\n")
                print(f" dealder Win") 
            else: 
                print("dealer and player has the same score")           
# card =Card("Space",5)

# card.show()

deck = Deck()
deck.build()
deck.show()
# deck.shuffle()

# ku=Player("KU")
# ku.draw(deck).draw(deck)  # we can draw many card as possible 
# ku.showhand()

# card =deck.draw()
# card.show()
