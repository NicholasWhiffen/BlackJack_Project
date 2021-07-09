import random
import db

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


#def getValue(hand):
    totalValue = 0
    for card in hand:
        if card[0] == "Q" or card[0] == "K" or card[0] == "J":
            totalValue += 10
        elif card[0] == "A":
            if (totalValue + 11) > 21:
                totalValue += 1
            else:
                totalValue += 11
        else:
            totalValue += int(card[0])
    return totalValue

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


def main():
    deck = createDeck()
    money = db.readMoney()
    playerHand = deal(deck)
    dealerHand = deal(deck)
    print(playerHand)
    print(dealerHand)
    addCard(playerHand, deck)
    addCard(dealerHand, deck)
    print(playerHand)
    print(dealerHand)
    print(getValue(playerHand))
if __name__ == "__main__":
    main()  