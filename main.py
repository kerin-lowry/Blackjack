############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
import art
from replit import clear

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards)==2:
        return 0
    if score > 21 and (11 in cards):
      cards.remove(11)
      cards.append(1)
    return sum(cards)       

def compare(user_s, computer_s):
    if computer_s == user_s:
        print("It's a draw.")
    elif computer_s == 0:
        print("Computer wins with Blackjack.")
    elif user_s == 0:
        print("User wins with Blackjack.")
    elif user_s > 21:
        print("You lose. You went over 21!")
    elif computer_s > 21:
        print("You win. Computer went over 21!")    
    elif user_s > computer_s:
        print("You win!")
    else:
        print("You lose. Computer was closer to 21.")              

def play():
    print(art.logo)
    user_cards = []
    user_score = 0

    computer_cards = []
    computer_score = 0

    game_over = False #check who wins in the end
    continue_deal = "y" #keep drawing cards

    #deal two cards each
    for i in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    #print(user_cards, computer_cards)
    #user_cards = [1, 10]
    #computer_cards = [10, 10]

    while game_over == False:
        user_score = calculate_score(user_cards)       
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards}, your score: {user_score}")
        print(f"Computer's first card [{computer_cards[0]}]")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            continue_deal = input("Would you like to draw another card? Type 'y' or 'n': ")
            if continue_deal == "y":
                user_cards.append(deal_card())
                print(user_cards)
            else:
                game_over = True        

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)



while input("Would you like to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play()