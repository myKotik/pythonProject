import random

attempts = 0

number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

while attempts < 5:
    guess = input("Take a guess ")
    guess = int(guess)
    attempts +=1

    if guess < number:
        print("Higher")

    if guess > number:
        print("Lower")

    if number == guess:
        print("You win")
        break
if guess == number:
        attempts = str(attempts)
        print(f"Good job! You guessed my number in {attempts} guesses!")
if guess != number:
        number = str(number)
        print(f"Nope. The number I was thinking of was {number}")