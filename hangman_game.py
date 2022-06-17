import random

words = ['hill','pony', 'house', 'car', 'company','suntan','prize','mist','fair','abundant','embark']
hidden_name = words[random.randrange(len(words))]
guessed_letters = []

# player input and checking if the letter is in list
rounds = 0
tries = 0
while tries<10:
    rounds += 1
    print(f"Round {rounds} ")
    print(f"You got {10 - tries} tries.")
    letter = input("Type a letter: ")

    # Check if the letter is not alphabetical or if there are multiple letters.
    while not letter.isalpha() or len(letter)>1:
        letter = input("Wrong input. Please try again. Type: ")

    #  Check if the letter is already guessed.
    while letter in guessed_letters:
        letter = input("You have already guessed this letter. Type: ")

    guessed_letters.append(letter)
    #print how many times the letter exists in the word
    counter = hidden_name.count(letter)
    if counter ==0:
        print(f"The letter '{letter}' does not exist.")
        tries += 1
    else:
        print(f"The letter '{letter}' exist {counter} times.")
    cnt = 0
    # check if the letter is in list
    for char in hidden_name:
        if char in guessed_letters:
            print(char,end='')
        else:
            print('_',end='')
            cnt += 1

    # check if the word is completely guessed.
    if cnt == 0:
        print('')
        print('Congratulations! You found the word!')
        break
    elif tries == 10:
        print('')
        print("You didn't find the word. Try again.")
    print('')