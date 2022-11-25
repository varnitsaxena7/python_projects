import random
name=input("Enter your name:\n").upper()
while True:
         range = input("Enter the range of numbers available for guesses:\n ")
         if range.isdigit():
             range = int(range)
             break
         else:
              print('Please type a number greater than 0 next time.\n')
              continue

answer= random.randint(0, range)
score = 0

while True:
    score =score+1
    guess = input("Guess the number: \n")
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please enter a number greater than 0 next time.\n')
        continue

    if guess == answer:
        break
    elif guess < answer:
        print("You guessed below the number!\n")
    else:
        print("You guessed above the number!\n")

print("\nYou guessed the number correctly.\n")
print("\n"+name+" guessed the number in "+str(score)+ " chances.")
