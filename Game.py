def display_word(w, guessing):  # changing names, because word and guessed are global variables
    for letter in w:
        print(letter if letter in guessing else '_', end=' ')  # make print shorter
    print()


def is_word_guessed(w, guessing):  # changing names, because word and guessed are global variables
    for letter in w:
        if letter not in guessing:
            return False
    return True


import random
words = ['python', 'programming', 'language', 'computer', 'disk', 'dock', 'data', ]
score = 0
while True:
    choice = input('You want to guess word? (y/n): ')
    if choice.lower() == 'y' and len(words) > 0:
        word = random.choice(words)
        guessed = []
        max_attempts = 6
        while max_attempts > 0:
            print(f'Your amount of tries: {max_attempts}.')
            guess = input('Enter letter: ').lower()
            if guess in guessed:
                print('You already asked this letter!')
            elif guess in word:
                guessed.append(guess)
                print(''.join(guessed))
                if is_word_guessed(word, guessed):
                    print(f'You won! Word was "{word}".')
                    score += 1
                    break
            else:
                print('There is no such letter in the hidden word.')
                max_attempts -= 1
        else:
            print(f'You lost. Word was "{word}".')
        words.remove(word)
    else:
        print(f'Thank for playing, your score: {score}.')
        break
