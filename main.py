from art import logo
import random

print(logo)

print("Welcome to the number guessing game!")
random_number = random.randint(1,101)

difficulty = input('Please select a difficulty. Type "easy" for 10 lives, or "hard" for 5\n')

if difficulty == "easy":
  LIVES = 10
else:
  LIVES = 5

def lose_life():
  return LIVES -1

print("I'm thinking of a number between 1 and 100")

def guess_number():
  global LIVES
  while LIVES > 0:
    guess = int(input("Make a guess\n"))
    if guess > random_number:
      print("Too high!")

    elif guess < random_number:
      print("Too low!")

    else:
      print("Congratulations! You win")
      break
      quit()
    LIVES = lose_life()
    print(f"You have {LIVES} lives left to guess the number.")
  else: 
    print(f"Unlucky! The number was {random_number}")
    quit()
  
guess_number()