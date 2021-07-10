import random
import db
import sys

print("BLACKJACK!")
print("Blackjack payout is 3:2")

def createDeck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    deck = []
    for suit in suits:
        value = 2
        for number in numbers:
            card = []
            card.append(value)
            card.append(suit)
            card.append(number)
            deck.append(card)
            value += 1
    return deck

def deal(deck):
    hand = []
    for card in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand

def addCard(hand, deck):
    newCard = deck.pop()
    hand.append(newCard)
    return hand

def getValue(hand):
    totalValue = 0
    for card in hand:
        #Value of King, Queen, Jack
        if card[0] == 11 or card[0] == 12 or card[0] == 13:
            totalValue += 10
        #Value of Ace
        if card[0] == 14:
            if (totalValue + 11) > 21:
                totalValue += 1
            else:
                totalValue += 11
        #Value of numbered cards
        else:
            totalValue += card[0]
    return totalValue

def showHand(hand):
    print("YOUR CARDS:")
    for card in hand:
        print(str(card[2]) + " of " + card[1])
    print()

#def checkWin(hand):
    #value = getValue(hand)
    #if value > 21:
        #print("BUST! You lose.")
        #print()#

def checkMoney(money):
    if len(money) == 0 or money[0] == 0:
        while True:
            try:
                addMoney = input("Your account balance is zero. Would you like to add more money? (y/n): ")
                if addMoney.lower() == "y":
                    amountMoneyAdded = int(input("How much money would you like to add?: "))
                    money.append(amountMoneyAdded)
                    print(str(amountMoneyAdded) + " was added to your account.")
                    db.writeMoney(money)
                    break
                elif addMoney.lower() == "n":
                    print("Thank you for playing.")
                    sys.exit()
                else:
                    print("Please enter y or n.")
            except ValueError:
                print("Please enter y or n")

def addMoney(money):
    while True:
        try:
            amountMoneyAdded = int(input("How much money would you like to add?: "))
            money[0] += amountMoneyAdded
            print(str(amountMoneyAdded) + " was added to your account.")
            db.writeMoney(money)
            print("Account balance is now: " + str(money[0]))
            break
        except ValueError:
            print("Please enter valid integer.")



def main():

    #Test code
    deck = createDeck()
    money = db.readMoney()
    checkMoney(money)
    print(money[0])
    playerHand = deal(deck)
    dealerHand = deal(deck)
    print(playerHand)
    print(dealerHand)
    addMoney(money)
    showHand(playerHand)

    #Game code
    while True:
        choice = input("Hit or stand? (hit/stand): ")
        print()
        if choice.lower() == "hit":
            addCard(playerhand, deck)
            showHand(playerhand)
            value = getValue(hand)
            if value > 21:
                print("BUST! You lose.")
                print("Money: " + str(money))
                break
        elif choice.lower() == "stand":

if __name__ == "__main__":
    main()  