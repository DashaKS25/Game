import random
words = ['python', 'programming', 'language', 'computer', 'disk', 'dock', 'data']
word = random.choice(words)
guessed = []
max_attempts = 6

def display_word(word, guessed):
    for letter in word:
        if letter in guessed:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

def is_word_guessed(word, guessed):
    for letter in word:
        if letter not in guessed:
            return False
    return True


while max_attempts > 0:
    print(f'У вас {max_attempts} попыток.')
    guess = input('Введите букву: ').lower()
    if guess in guessed:
        print('Вы уже угадали эту букву!')
    elif guess in word:
        guessed.append(guess)
        print("".join(guessed))
        if is_word_guessed(word, guessed):
            print(f'Вы победили! Загаданное слово было "{word}".')
            break
    else:
        print('Такой буквы нет в загаданном слове.')
        max_attempts -= 1
else:
    print(f'Вы проиграли. Загаданное слово было "{word}".')

