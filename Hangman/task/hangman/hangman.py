import random


def show_menu():
    print()
    select = input('Type "play" to play the game, "exit" to quit: ')
    if select == 'play':
        play()
        print()
    elif select == "exit":
        quit()
    else:
        pass


def play():
    tries = 8
    words = ['python', 'java', 'kotlin', 'javascript']
    guess_word = random.choice(words)
    output = list("-" * (len(guess_word)))
    letters_guessed = set()
    letters_already_guessed = set()
    won = False

    while tries > 0:
        output_string = "".join(output)
        if output_string == guess_word:
            won = True
            break

        print()
        print(output_string)
        guess_letter = input("Input a letter: ")

        if guess_letter in guess_word:
            if guess_letter in letters_guessed:
                print("You already typed this letter")

            letters_guessed.update(guess_letter)
            letters_already_guessed.update(guess_letter)
            for j in range(len(guess_word)):
                if guess_word[j] == guess_letter:
                    output[j] = guess_letter
                    j = j + 1
        elif len(guess_letter) != 1:
            print("You should input a single letter")
        elif not guess_letter.islower():
            print("It is not an ASCII lowercase letter")
        elif guess_letter in letters_guessed or guess_letter in letters_already_guessed:
            print("You already typed this letter")
        else:
            tries = tries - 1
            letters_already_guessed.update(guess_letter)
            print("No such letter in the word")

    if won:
        print("You guessed the word!")
        print("You survived!")
        show_menu()
    else:
        print("You lost!")
        print()
        show_menu()


print("H A N G M A N")
show_menu()
