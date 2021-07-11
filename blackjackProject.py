import random
import db
import sys

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
        elif card[0] == 14:
            if (totalValue + 11) > 21:
                totalValue += 1
            else:
                totalValue += 11
        #Value of numbered cards
        else:
            totalValue += card[0]
    return totalValue

def showHand(hand):
    for card in hand:
        print(str(card[2]) + " of " + card[1])
    print()

def checkMoney(money):
    if len(money) == 0 or money[0] < 5:
        while True:
            try:
                addMoney = input("Your account balance is does not have enough for minimum bet. Would you like to add more money? (y/n): ")
                if addMoney.lower() == "y":
                    amountMoneyAdded = float(input("How much money would you like to add?: "))
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
            amountMoneyAdded = float(input("How much money would you like to add?: "))
            money[0] += amountMoneyAdded
            print(str(amountMoneyAdded) + " was added to your account.")
            db.writeMoney(money)
            print("Account balance is now: " + str(money[0]))
            break
        except ValueError:
            print("Please enter valid integer.")

def makeBet(money):
    while True:
        try:
            checkMoney(money)
            bet = float(input("Enter bet amount: "))
            if bet < 5 or bet > 1000:
                print("Bet must be between 5 and 1000")
            elif bet > money[0]:
                print("Not enough money to make bet. Choose again")
            else:
                money[0] -= bet
                db.writeMoney(money)
                return bet
        except ValueError:
            print("Enter a valid integer")

def dealerMoves(hand, deck):
    while True:
        value = getValue(hand)
        if value < 17:
            addCard(hand, deck)
        else:
            break

def checkWin(pHand, dHand, money, bet):
    playerScore = getValue(pHand)
    dealerScore = getValue(dHand)
    if playerScore > 21:
        print("YOUR POINTS: " + str(playerScore))
        print("DEALER POINTS: " + str(dealerScore))
        print()
        print("BUST! You lose.\n")
    elif dealerScore > 21:
        print("YOUR POINTS: " + str(playerScore))
        print("DEALER POINTS: " + str(dealerScore))
        print()
        print("DEALER BUST! You win.\n")
        money[0] += (bet * 1.5)
        db.writeMoney(money)
    elif dealerScore < 21 and playerScore < 21:
        if playerScore > dealerScore:
            print("YOUR POINTS: " + str(playerScore))
            print("DEALER POINTS: " + str(dealerScore))
            print()
            print("You win.\n")
            money[0] += (bet * 1.5)
            db.writeMoney(money)
        else:
            print("YOUR POINTS: " + str(playerScore))
            print("DEALER POINTS: " + str(dealerScore))
            print()
            print("You lose.\n")
    elif dealerScore == playerScore:
        print("YOUR POINTS: " + str(playerScore))
        print("DEALER POINTS: " + str(dealerScore))
        print()
        print("Draw.")
        money[0] += bet
        db.writeMoney(money)


def main():
    money = db.readMoney()
    checkMoney(money)

    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    playAgain = "y"
    while playAgain.lower() == "y":
        deck = createDeck()
        print("Money: " + str(money[0]))
        bet = makeBet(money)
        print("Bet amount: " + str(bet))
        print()

        dealerHand = deal(deck)
        playerhand = deal(deck)
        print("DEALER'S SHOW CARD:")
        print(str(dealerHand[0][2]) + " of " + str(dealerHand[0][1]) + "\n")
        print("YOUR CARDS:")
        showHand(playerhand)

        while True:
            try:
                choice = input("Hit or stand? (hit/stand): ")
                print()
                if choice.lower() == "hit":
                    addCard(playerhand, deck)
                    showHand(playerhand)
                    value = getValue(playerhand)
                    if value > 21:
                        break
                elif choice.lower() == "stand":
                    break
                else:
                    print("Please enter hit or stand")
            except ValueError:
                print("Please enter hit or stand")
        dealerMoves(dealerHand, deck)
        checkWin(playerhand, dealerHand, money, bet)
        while True:
            try:
                playAgain = input("Play again? (y/n): ")
                if playAgain.lower() == "y":
                    break
                elif playAgain.lower() == "n":
                    break
                else:
                    print("Must enter y or n")
            except ValueError:
                print("Must enter y or n")
    print("Come back soon!\nBye!")
            
if __name__ == "__main__":
    main()  