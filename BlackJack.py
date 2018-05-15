from IPython.display import clear_output
import random
import time

class Cards:
    def __init__(self, cardtype, value, image):
        self.cardtype = cardtype
        self.value = int(value)
        self.image = image

        
#Deck of Cards
acecard = Cards('Ace',11,' _______ \n|A      |\n|       |\n|   *   |\n|       |\n|\033[4m      A\033[0m|')
twocard = Cards('Two',2,' _______ \n|2      |\n|   *   |\n|       |\n|   *   |\n|\033[4m      2\033[0m|')
threecard = Cards('Three',3,' _______ \n|3  *   |\n|       |\n|   *   |\n|       |\n|\033[4m   *  3\033[0m|')
fourcard = Cards('Four',4,' _______ \n|4*   * |\n|       |\n|       |\n|       |\n|\033[4m *   *4\033[0m|')
fivecard = Cards('Five',5,' _______ \n|5*   * |\n|       |\n|   *   |\n|       |\n|\033[4m *   *5\033[0m|')
sixcard = Cards('Six',6,' _______ \n|6*   * |\n|       |\n| *   * |\n|       |\n|\033[4m *   *6\033[0m|')
sevencard = Cards('Seven',7,' _______ \n|7*   * |\n|   *   |\n| *   * |\n|       |\n|\033[4m *   *7\033[0m|')
eightcard = Cards('Eight',8,' _______ \n|8*   * |\n|   *   |\n| *   * |\n|   *   |\n|\033[4m *   *8\033[0m|')
ninecard = Cards('Nine',9,' _______ \n|9*   * |\n| *   * |\n|   *   |\n| *   * |\n|\033[4m *   *9\033[0m|')
tencard = Cards('Ten',10,' _______ \n|1*   * |\n|0*   * |\n| *   * |\n| *   *1|\n|\033[4m *   *0\033[0m|')
jackcard = Cards('Jack',10,' _______ \n|J      |\n|       |\n| Jack  |\n|       |\n|\033[4m      J\033[0m|')
queencard = Cards('Queen',10,' _______ \n|Q      |\n|       |\n| Queen |\n|       |\n|\033[4m      Q\033[0m|')
kingcard = Cards('King',10,' _______ \n|K      |\n|       |\n| King  |\n|       |\n|\033[4m      K\033[0m|')
blankcard = Cards('Blank',0,' _______ \n| XXXXX |\n|XXXXXXX|\n|XXXXXXX|\n|XXXXXXX|\n|\033[4m XXXXX \033[0m|')


deck = [acecard,twocard,threecard,fourcard,fivecard,sixcard,sevencard,eightcard,ninecard,tencard,jackcard,queencard,kingcard]*4
dealerhand = []
playerhand = []

class Money:
    def __init__(self, playerpool=3200, betpool=0):
        self.playerpool = int(playerpool)
        self.betpool = int(betpool)
    
    def bet(self, betamount=0):
        while True:
            try:
                betamount = int(input(f'Balance: {self.playerpool}\nPlease place a bet: '))
                while int(betamount) > self.playerpool:
                    print ("You don't have enough money!")
                    betamount = int(input("Please bet again: "))
                    continue
                while int(betamount) < 10:
                    print ("The minimum bet is 10!")
                    betamount = int(input("Please bet again: "))
                    continue
                if int(betamount) <= self.playerpool:
                    self.betpool += int(betamount)
                    self.playerpool -= betamount
                    break
            except:
                print('That is not a number')
    
    def lose(self):
        self.betpool = 0
    
    def win(self):
        self.playerpool += (self.betpool*2)
        self.betpool = 0
        
    def tie(self):
        self.playerpool += self.betpool
        self.betpool = 0
            
                
player1 = Money()

            
def printBoard():
    clear_output()
    print("Dealer's Hands:")
    for l in zip(*dealerlines):
        print(*l,sep='  ')
    print("\nYour Hand:")
    for l in zip(*playerlines):
        print(*l,sep='  ')
    print(f'Your bet was: {player1.betpool}')
    print(f'Your Balance is: {player1.playerpool}')
    
    

        
def hitOrStay():
    while True:
        global turn
        hitstay = input("Do you want to hit or stay? ")
        if hitstay.lower() == 'hit':
            playerhand.append(deck.pop())
            playerlines.append(playerhand[-1].image.splitlines())
            printBoard()
            loseCheck()
            if turn == 'Restart':
                break
            
        if hitstay.lower() == 'stay':
            turn = 'Dealer'
            loseCheck()
            break
            
        
def loseCheck():
    playerhandtotal = 0
    global turn
    global playerace
    for card in playerhand:
        playerhandtotal += card.value
    if playerace == True:
        playerhandtotal -= 10
    if sum (card == acecard for card in playerhand) == 2 and playerhandtotal > 21:
        playerhandtotal -= 10
    if playerhandtotal > 21 and acecard in playerhand and playerace == False:
        playerace = True
        playerhandtotal -= 10
    if playerhandtotal > 21:
        player1.lose()
        print ('\nBUST\nYou Lose.')
        turn = 'Restart'
    else:
        global playerhandvalue
        playerhandvalue = playerhandtotal
        

def naturalCheck():
    global hands
    global dealerlines
    if (dealerhand[0].value + dealerhand[1].value) == 21 and (playerhand[0].value + playerhand[1].value) == 21:
        dealerlines = [dealerhand[0].image.splitlines(),dealerhand[1].image.splitlines()]
        printBoard()
        player1.tie()
        print ('\nYou both got BlackJack!!! What are the chances?')
        hands = 'Natural'
    
    elif (dealerhand[0].value + dealerhand[1].value) == 21:
        dealerlines = [dealerhand[0].image.splitlines(),dealerhand[1].image.splitlines()]
        printBoard()
        player1.lose()
        print ('\nDealer has BlackJack!')
        hands = 'Natural'

    elif playerhand[0].value + playerhand[1].value == 21:
        printBoard()
        player1.win()
        print ('\nYou got BlackJack!!!')
        hands = 'Natural'
    else:
        printBoard()
        
def dealerTurn():
    while True:
        global dealerace
        dealerhandtotal = 0
        for card in dealerhand:
            dealerhandtotal += card.value
        if dealerace == True:
            dealerhandtotal -= 10
        if sum (card == acecard for card in dealerhand) == 2 and dealerhandtotal > 21:
            dealerhandtotal -= 10
        if dealerhandtotal < 17:
            dealerhand.append(deck.pop())
            dealerlines.append(dealerhand[-1].image.splitlines())
            printBoard()
            time.sleep(2)
            continue
        elif dealerhandtotal >= 17 and dealerhandtotal <= 21:
            global dealerhandvalue
            dealerhandvalue = dealerhandtotal
            print (dealerhandvalue)
            printBoard()
            break
        elif dealerhandtotal > 21 and acecard in dealerhand and dealerace == False:
            dealerace = True
            dealerhandtotal -= 10
            continue
        if dealerhandtotal > 21:
            global turn
            printBoard()
            print ('\nDealer bust.')
            turn = 'Restart'
            break
                    
            
def lengthCheck(something):
    totallength = 0
    for item in something:
        totallength += 1
    return totallength
        
        
#Shuffle the deck
random.shuffle(deck)

#Deal the deck
#playerhand = []
#dealerhand = []
#playerhand.append(deck.pop())
#dealerhand.append(deck.pop())
#playerhand.append(deck.pop())
#dealerhand.append(deck.pop())

if False:
    print(acecard.image) 
    print(twocard.image)
    print(threecard.image)
    print(fourcard.image)
    print(fivecard.image)
    print(sixcard.image)
    print(sevencard.image)
    print(eightcard.image)
    print(ninecard.image)
    print(tencard.image)
    print(jackcard.image)
    print(queencard.image)
    print(kingcard.image)
    print(blankcard.image)
    pass

#Seperates the card image by lines and stitches it back together so it can be side-by-side

#dealerlines = [dealerhand[0].image.splitlines(),blankcard.image.splitlines()]
#playerlines = [playerhand[0].image.splitlines(),playerhand[1].image.splitlines()]
playerhandvalue = 0
dealerhandvalue = 0
                                                  
while True:
    
    if player1.playerpool < 10:
        print ('Sorry you have too little funds to continue... Thanks for playing!')
        break
    playerace = False
    dealerace = False
    lengthCheck(deck)
    if lengthCheck(deck) < 10:
        deck = [acecard,twocard,threecard,fourcard,fivecard,sixcard,sevencard,eightcard,ninecard,tencard,jackcard,queencard,kingcard]*4
        random.shuffle(deck)
    
    playerhandvalue = 0
    dealerhandvalue = 0
    playerhand = []
    dealerhand = []
    playerhand.append(deck.pop())
    dealerhand.append(deck.pop())
    playerhand.append(deck.pop())
    dealerhand.append(deck.pop())
        
    
    dealerlines = [dealerhand[0].image.splitlines(),blankcard.image.splitlines()]
    playerlines = [playerhand[0].image.splitlines(),playerhand[1].image.splitlines()]

    turn = 'Start'
    hands = 'undecided'
    player1.bet()
    naturalCheck()
    if hands == 'Natural':
        continue
    else:
        hitOrStay()
        
        #if turn == 'Restart':
            #continue
        while turn == 'Dealer':
            dealerlines = [dealerhand[0].image.splitlines(),dealerhand[1].image.splitlines()]
            dealerTurn()
            if dealerhandvalue > playerhandvalue:
                player1.lose()
                print('\nYou lose~')
                turn = 'Start'
            elif playerhandvalue > dealerhandvalue:
                player1.win()
                print('\nYou win!')
                turn = 'Start'
            
            elif playerhandvalue == dealerhandvalue:
                player1.tie()
                print("\nIt's a tie")
                turn = 'Start'
                
    