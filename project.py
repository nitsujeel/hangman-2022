from random import randint
from csv import reader


CATS = ["FRUITS", "SPORTS", "COLOURS", "ANIMALS"]
DIFF = ["EASY", "MEDIUM", "HARD"]
GUESSED = [] #for all letters guessed
RIGHT = [] #for letters guessed correctly only (i.e. letters in word)


def main():
    #choose difficulty
    while True:
        print("Choose a difficulty:", *DIFF)
        d = input().upper()
        if d not in DIFF:
            print("Invalid difficulty.")
        else:
            break
    #choose category
    while True:
        print("Choose a category:", *CATS)
        cat = input().upper()
        if cat not in CATS:
            print("Invalid category.")
        else:
            break
    #select random word
    list = []
    with open(f"{cat}.txt") as lib:
        rdr = reader(lib)
        for row in rdr:
            list.append(row[0])
    word = list[randint(0, len(list) - 1)]
    #pturn until win or lose
    state = 0
    while True:
        print(wordstate(word))
        print("Letters guessed:", *sorted(GUESSED))
        while True:
            letter = input("Guess a letter: ").upper()
            if len(letter) == 1 and letter.isalpha() and letter not in GUESSED:
                break
            else:
                print("Please input a valid letter that has not been guessed yet.")
                print("Letters guessed:", *sorted(GUESSED))
        if check(letter, word):
            print(f"{letter} is in the word!")
            if "_" not in wordstate(word):
                print(wordstate(word))
                print("You win!")
                break
        else:
            print(f"{letter} is not in the word...")
            if d == "EASY":
                state += 1
            elif d == "MEDIUM":
                state += 2
            else:
                state += 3
            print(man(state))
            if state == 12:
                print(f"You lose. The answer is {word}.")
                break


def wordstate(word):
    #returns the revealed and hidden letters in current state
    toreturn = []
    for char in word:
        if char.isalpha():
            if char in RIGHT:
                toreturn.append(f"{char} ")
            else:
                toreturn.append("_ ")
        else:
            toreturn.append(" ")
    return "".join(toreturn)


def man(state):
    #returns man to print according to state
    if state == 0:
        return ""
    elif state == 1:
        return "========="
    elif state == 2:
        return "       \n       \n       \n       \n      |\n      |\n========="
    elif state == 3:
        return "       \n       \n      |\n      |\n      |\n      |\n========="
    elif state == 4:
        return "      +\n      |\n      |\n      |\n      |\n      |\n========="
    elif state == 5:
        return "  +---+\n      |\n      |\n      |\n      |\n      |\n========="
    elif state == 6:
        return "  +---+\n  |   |\n      |\n      |\n      |\n      |\n========="
    elif state == 7:
        return "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n========="
    elif state == 8:
        return "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n========="
    elif state == 9:
        return "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n========="
    elif state == 10:
        return "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n========="
    elif state == 11:
        return "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n========="
    elif state == 12:
        return "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="


def check(letter, word):
    #checks if letter is in word, returns true or false and updates guessed, right lists
    GUESSED.append(letter)
    if letter in word:
        RIGHT.append(letter)
        return True
    else:
        return False


if __name__ == "__main__":
    main()