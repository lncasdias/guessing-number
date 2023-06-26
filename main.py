import random

low = guesses = 0
high = 999 # need to learn how to make the high variable empty
feedback = ' '
while feedback != 'c':
    guess = random.randint(low, high)
    feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)? ').lower().strip()
    if feedback == 'h':
            high = guess - 1
    elif feedback == 'l':
            low = guess + 1
    guesses += 1
print (f'Hurray! The computer guessed the number {guess} correctly! It took {guesses} attempts to guesses, oof!')
