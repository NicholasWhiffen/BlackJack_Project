import random

print("BLACKJACK!")
print("Blackjack payout is 3:2")

MONEY = "money.txt"

def createDeck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = []
    for suit in suits:
        for number in numbers:
            deck.append(suit + " of " + number)
    return deck

def readMoney():
    while True:
        try:
            money = []
            with open(MONEY, "r") as file:
                for line in file:
                    line = line.replace("\n", "")
                    money.append(line)
            return money
        except FileNotFoundError:
            print("Could not find money file!")
            print("Starting new money file...\n")
            with open(MONEY, "w") as file:
                file.write("")

def writeMoney(money):
    with open(MONEY, "w") as file:
        for item in money:
            file.write(item + "\n")

def deal(cards):
    for card in range(2):
        hand = []
        card = []
        random.shuffle(cards[0])
        random.shuffle(cards[1])
        cardValue = cards[0].pop()
        cardSuit = cards[1].pop()
        card.append(cardSuit)
        card.append(cardValue)
        hand.append(card)
    return hand
    

def main():
    deck = createDeck()
    money = readMoney()
    hand = deal(cards)
    hand = deal(cards)
    print(hand)


if __name__ == "__main__":
    main()  