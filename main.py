from random import randint
from art import logo
level = {
'easy': 10,
'hard':5,
}

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

real_number = randint(0, 101)
# guess = int(input("Make a guess: "))
def keep_playing():	
	attempts = level[difficulty]
	guess = int(input("Make a guess: "))
	if attempts > 0:
		if guess !=  real_number:				
			level[difficulty] -= 1
			if guess < real_number:
				print("Too low.")					
				keep_playing()			
			if guess > real_number:
				print("Too high.")
				keep_playing()
		elif guess == real_number:
			print("Congratulations!")
			print(f"Number of attempts left:{attempts}")
			return print("You got it!")

	else:
		if attempts <= 0 and guess != real_number:
			print(f"Number of attempts left:{attempts}")
			return print("You've run out of guesses, you lose.")
			
		elif guess == real_number:
			print("Congratulations!")
			print(f"Number of attempts left:{attempts}")
			return print("You got it!")

print(f"Hint, the number is: {real_number}")
keep_playing()
print('final')
	
