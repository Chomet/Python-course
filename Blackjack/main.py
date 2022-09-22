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
from art import logo

##from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
yourcards = []
compcards = []
yourscore = 0
compscore = 0


def total(cardslist):
    cardsscore = 0
    for n in cardslist:
        cardsscore += n
    return cardsscore


def check_blackjack_and_22(yourscore, compscore):
    if compscore == 22:
        compcards[0] = 1
    if yourscore == 22:
        yourcards[0] = 1
    if compscore == 21:
        print(f"    You got {yourcards}")
        print(f"    Computer got {compcards}, this is a Blackjack, you lose!")
        return True
    elif yourscore == 21:
        print(f"    You got {yourcards}, this is a Blackjack, you win!")
        print(f"    Computer got {compcards}")
        return True
    else:
        print(f"    Your cards: {yourcards}, current score: {total(yourcards)}")
        print(f"    Computer's first card: {compcards[0]}")
        return False


def check_aces(cardslist):
    print("Checking aces")
    for n in range(0, len(cardslist)):
        if cardslist[n] == 11:
            cardslist[n] = 1
            break


def initial_hand():
    yourcards.append(random.choice(cards))
    yourcards.append(random.choice(cards))
    compcards.append(random.choice(cards))
    compcards.append(random.choice(cards))
    yourscore = total(yourcards)
    compscore = total(compcards)
    return check_blackjack_and_22(yourscore, compscore)


def human_move():
    while True:
        cont = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if cont == "n":
            return False
        yourcards.append(random.choice(cards))
        yourscore = total(yourcards)
        if yourscore > 21:
            check_aces(yourcards)
            yourscore = total(yourcards)
            if yourscore > 21:
                print(f"    Your cards: {yourcards}, final score: {yourscore}, you are over 21")
                print(f"    Computer got {compcards}")
                print("You lose!")
                return True
            else:
                print(f"    Your cards: {yourcards}, current score: {yourscore}")
                print(f"    Computer's first card: {compcards[0]}")
        else:
            print(f"    Your cards: {yourcards}, current score: {yourscore}")
            print(f"    Computer's first card: {compcards[0]}")


def comp_move():
    while True:
        yourscore = total(yourcards)
        compscore = total(compcards)
        if compscore > 16:
            print(f"    Your cards: {yourcards}, final score: {yourscore}")
            print(f"    Computer got {compcards}, final score: {compscore}")
            if yourscore > compscore:
                print("You win!")
                return
            else:
                print("You lose!")
                return
        else:
            compcards.append(random.choice(cards))
            compscore = total(compcards)
            if compscore > 21:
                check_aces(compcards)
                compscore = total(compcards)
                if compscore > 21:
                    print(f"    Your cards: {yourcards}, final score: {yourscore}")
                    print(f"    Computer got {compcards}, he is over 21")
                    print("You win!")
                    return


while True:
    cont = input("Do you want to play Blackjack (y or n): ").lower()
    if cont == "n":
        break
    ##clear()
    print(logo)
    if not initial_hand():
        if not human_move():
            comp_move()
    yourcards = []
    compcards = []
    yourscore = 0
    compscore = 0