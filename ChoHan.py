import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}
STARTING_MONEY = 5000
COMMISSION = 40


def make_bet(money):
    while True:
        try:
            bet = int(input(f"You have {money} mon. How much do you want to bet? (Or type -1 to quit)\n > "))
            if bet == -1:
                input("Press Enter to exit...")
                sys.exit()
            if 0 < bet <= money:
                return bet
            else:
                print("You cannot bet more then you have!\n")
                return make_bet(money)
        except ValueError:
            print("Invalid input")
            return make_bet(money)


def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)


def main():
    money = STARTING_MONEY
    while money > 0:
        bet = make_bet(money)

        print("The dealer swirls the cup and you hear the rattle of dice"
              "\nThe dealer slams the cup on the floor, still covering the dice and asks for your bet.")
        dice1, dice2 = roll_dice()
        total = dice1 + dice2
        result = 'cho' if total % 2 == 0 else 'han'

        print("CHO (even) or HAN (odd)?")
        choice = input("> ").strip().lower()
        if choice not in ['cho', 'han']:
            print("Invalid input. Enter 'cho' or 'han'.\n")
            continue

        print("The dealer lifts the cup to reveal:")
        print(f"{JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]}")
        print(f"{dice1} - {dice2}")

        if choice == result:
            print(f"You won! You take {bet} mon. The house collects a 40 mon fee.")
            money += (bet - COMMISSION)
        else:
            print("You lost!")
            money -= bet

        print()

    print("You have run out of money. Game over!")
    input("Press any button")


if __name__ == '__main__':
    main()
