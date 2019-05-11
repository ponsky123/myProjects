from IPython.display import clear_output
import random
import copy
import time

class Player():  
    def __init__(self,balance=1000, name='Player'):
        self.balance = balance
        self.hand = []
        self.name = name
        
    def __str__(self):
        return self.hand
    
    def hand_sum(self):
        player1 = copy.deepcopy(self.hand)
        player_sum = 0
        player_sum2 = 0
        flag = False
        
        # change face value cards to 10
        for i in range(len(player1)):
            if player1[i] > 10:
                player1[i] = 10
        
        # turns all Aces to 11 initially
        for i in range(len(player1)):
            if player1[i] == 1:
                player1[i] = 11
        
        # takes current summation
        for i in range(len(player1)):
            player_sum = player_sum + player1[i]
        
        # turns Aces over sum to 1, one by one
        for i in range(len(player1)):
            if player_sum >= 22 and player1[i] == 11:
                player1[i] = 1
                flag = True
            player_sum2 = player_sum2 + player1[i]
        
        if flag == True:
            return player_sum2
        else:
            return player_sum  

class Deck():
    import random
    
    def __init__(self):
        full_deck_list = []
        self.full_deck_list = full_deck_list
        for i in range(1,14):
            for j in range(4):
                self.full_deck_list = self.full_deck_list + [i]
                
    def __len__(self):
        return len(self.full_deck_list)
    
    def shuffle(self):
        random.shuffle(self.full_deck_list)
        
    def deal(self):
        card = self.full_deck_list[0]
        self.full_deck_list.pop(0)
        return card
    
def card_display_human(human_player):
    player1 = copy.deepcopy(human_player)
    for i in range(len(human_player)):
        if human_player[i] == 1:
            player1[i] = 'A'
        elif human_player[i] == 11:
            player1[i] = 'J'
        elif human_player[i] == 12:
            player1[i] = 'Q'
        elif human_player[i] == 13:
            player1[i] = 'K'
    
    print('Your cards are: %s' % ','.join([str(e) for e in player1]))
    print('--------------------------')

def card_display_computer(computer_player):
    player1 = copy.deepcopy(computer_player)
    for i in range(len(computer_player)):
        if computer_player[i] == 1:
            player1[i] = 'A'
        elif computer_player[i] == 11:
            player1[i] = 'J'
        elif computer_player[i] == 12:
            player1[i] = 'Q'
        elif computer_player[i] == 13:
            player1[i] = 'K'
            
    return player1

def again():
    return input('Do you want to play again?: ').lower()

# Player Ready
'''
game_on = input("Ready to play? [Yes] or [No]: ")
while game_on != 'Yes' and game_on != 'No' and game_on != 'yes' and game_on != 'no':
    print('Incorrect input')
    game_on = input("Ready to play? [Yes] or [No]: ")
'''
human_player = Player()
human_player.name = input('What is your name?: ')
game_on = 'yes'
# 1 game round
while game_on.lower() == 'yes':
    
    # initialize game setup and player bet
    human_player.hand = []
    computer_player = Player(balance=1000000)
    deck = Deck()
    dealer_deck = []
    flag2 = False
    
    print('Welcome '+ human_player.name + ', let\'s play Blackjack.')
    bet = int(input('Enter the amount you would like to bet [1-{}]: '.format(human_player.balance)))
    while bet > human_player.balance or bet <= 0:
       print('Incorrect bet amount.')
       bet = int(input('Enter the amount you would like to bet [1-1000]: '))

    clear_output()
    
    # deal out cards
    deck.shuffle()
    for i in range(2):
        human_player.hand.append(deck.deal())
        computer_player.hand.append(deck.deal())
    
    # show initial hands (players and dealer)
    card_display_human(human_player.hand)
    print('Your Sum: ' + str(human_player.hand_sum()))
    print('\n\n')
    x1,x2 = card_display_computer(computer_player.hand)
    print('Dealer cards are: {},X'.format(x1))
    print('--------------------------')
    
    # hit or stay
    choice = input('Would you like to [hit] or [stay]?: ')
    while choice != 'hit' and choice != 'stay':
        choice = input('Would you like to [hit] or [stay]?: ')
    
    while choice == 'hit':
        human_player.hand.append(deck.deal())
        clear_output()
        card_display_human(human_player.hand)
        print('Your Sum: ' + str(human_player.hand_sum()))
        print('\n\n')
        x1,x2 = card_display_computer(computer_player.hand)
        print('Dealer cards are: {},X'.format(x1))
        print('--------------------------')
        if human_player.hand_sum() > 21:
            print('\nBUST! You went over 21.')
            flag2 = True
            break
        choice = input('Would you like to [hit] or [stay]?: ')
        while choice != 'hit' and choice != 'stay':
            choice = input('Would you like to [hit] or [stay]?: ')
    
    if human_player.hand_sum() <= 21:
        clear_output()
        card_display_human(human_player.hand)
        print('Your Sum: ' + str(human_player.hand_sum()))
        print('\n\n')
        x1,x2 = card_display_computer(computer_player.hand)
        print("Dealer cards are: ", end =" ")
        time.sleep(2)
        print(x1, x2)
        print('--------------------------')
        print('Dealer Sum: ' + str(computer_player.hand_sum()))
        time.sleep(4)
        while computer_player.hand_sum() < 17:
            computer_player.hand.append(deck.deal())
            clear_output()
            card_display_human(human_player.hand)
            print('Your Sum: ' + str(human_player.hand_sum()))
            print('\n\n')
            dealer_deck = card_display_computer(computer_player.hand)
            print("Dealer cards are: ", end =" ")
            time.sleep(2)
            for i in range(len(dealer_deck)):
                print(dealer_deck[i], end =" ")
                time.sleep(1)
            print("")
            print('--------------------------')
            print('Dealer Sum: ' + str(computer_player.hand_sum()))
            time.sleep(2)
    
    if flag2 == False:
        print('\nRESULT: ', end=" ")
        if human_player.hand_sum() > computer_player.hand_sum() or computer_player.hand_sum() > 21:
            print('You win!')
            human_player.balance = human_player.balance + 2*bet
        elif human_player.hand_sum() < computer_player.hand_sum():
            print('You lose!')
            human_player.balance = human_player.balance - 2*bet
        elif human_player.hand_sum() == computer_player.hand_sum():
            print('Draw!')
            human_player.balance = human_player.balance + bet
    else:
        human_player.balance = human_player.balance - (2*bet)
      
    print("Balance left: " + str(human_player.balance))
    if human_player.balance <= 0:
        print('You are out of money fool, get out.')
        break
    game_on = again()


print('\nGoodbye ' + human_player.name + ', Thanks for playing.')
