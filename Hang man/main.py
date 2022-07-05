import random
import time

print("Welcome to Hangman game made by Harsh Kumar")
time.sleep(2)
print("Enter your name : ")
Name = input()
time.sleep(1)

print(f"Welcom, {Name}. The game is about to start")


def draw():
    global count
    if count == 1:
        print('''
         _____
        |
        |
        |
        |
        |
        |
      __|__
        ''')

    elif count == 2:
        print('''
         _____
        |     |
        |
        |
        |
        |
        |
      __|__
        ''')

    elif count == 3:
        print('''
         _____
        |     |
        |     O
        |
        |
        |
        |
      __|__
        ''')

    elif count == 4:
        print('''
         _____
        |     |
        |     |
        |     O
        |    /|\\
        |     
        |
      __|__
        ''')

    elif count == 5:
        print('''
         _____
        |     |
        |     |
        |     O
        |    /|\\
        |     |
        |    / \\
      __|__
        ''')


def main():
    global word
    global display
    global already_guessed
    global count
    global original_word
    global length
    words = ["january", "border", "image", "film",
             "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
    word = random.choice(words)
    original_word = word[:]
    length = len(word)
    display = "_" * length
    already_guessed = []
    count = 0


def play_again():
    inpu = input(" Do you want to play again (y/n)")
    if inpu == 'y':
        loop()

    else:
        print("Thanks for playing game")
        exit()


def hangman():
    global word
    global display
    global already_guessed
    global limit
    global original_word
    global count
    limit = 5
    print(f"Your word is : {display}\n")
    guess = input("Enter your guess : ")
    if len(guess) == 0 or len(guess) > 1 or guess.isnumeric():
        print("Please enter a valid alphaped")
        hangman()

    elif guess in word:
        already_guessed.append(guess)
        index = word.find(guess)
        word = word[:index] + "_" + word[index+1:]
        display = display[:index] + guess + display[index+1:]

    elif guess in already_guessed:
        print("You already guessed this, try another one")

    else:
        count += 1
        draw()
        if count == 1 or count == 2 or count == 3:
            print(f"Wrong guess. Only {limit-count} chance left")

        elif count == 4:
            print("Wrong guess. last chance ")
        elif count == 5:
            print("Wrong guess. you are hanged ")
            print(f"The word was {original_word}")
            play_again()

    if word == "_" * length:
        (f"Congrulation you guess the word {original_word}")
        play_again()

    elif count != limit:
        hangman()


def loop():
    main()
    hangman()


loop()
