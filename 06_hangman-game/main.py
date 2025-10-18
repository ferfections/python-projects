import random

def main():
    wordsList = ['tree', 'house', 'moon', 'understand', 'game']
    chosen = random.choice(wordsList)
    print("The word has been chosen.")

    guessed = False

    while guessed is False:
        letter = ""

        res = ""
        for i in chosen:
            if letter == i:
                res += letter
            else:
                res += "_"
        print(res)
        letter = input("Make your guess: ")

main()
