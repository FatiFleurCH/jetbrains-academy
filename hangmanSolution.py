import random

words = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
# Ask the user if they want to play
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "play":
        game_word = random.choice(words)
        chosen = set(game_word)
        length = len(game_word)
        guess = ["-" for l in game_word]
        attempts = 8
        attempted = []   
        while attempts > 0:
            print()
            print("".join(guess))
            letter = input("Input a letter: ")
            # Check if the input is a an ASCII lowercase letter
            # Check if the input is a single letter
            # Check if the input has not been typed already
            if not letter.islower() and len(letter) != 1:
                print("It is not an ASCII lowercase letter")
                print("You should print a single letter")
                continue
            if not letter.islower():
                print("It is not an ASCII lowercase letter")
                continue
            if len(letter) != 1:
                print("You should print a single letter")
                continue
            if letter in attempted:
                print("You already typed this letter")
                continue
            # Check if the letter is indeed a correct guess
            # If it is it is added to the guess list (----)
            if letter in chosen:
                for i in range(length):
                    if letter == game_word[i]:
                        guess[i] = game_word[i]
                chosen.discard(letter)
            # If not you lose a life
            else:
                print("No such letter in the word")
                attempts -= 1
            attempted.append(letter)
        if "-" in set(guess):
            print("You are hanged!")
        else:
            print("You survived!")
    elif menu == "exit":
        break
    
