MONEY = "money.txt"

def readMoney():
    while True:
        try:
            money = []
            with open(MONEY, "r") as file:
                for line in file:
                    line = line.replace("\n", "")
                    money.append(float(line))
            return money
        except FileNotFoundError:
            print("Could not find money file!")
            print("Starting new money file...\n")
            with open(MONEY, "w") as file:
                file.write("0")

def writeMoney(money):
    with open(MONEY, "w") as file:
        for item in money:
            file.write(str(item) + "\n")