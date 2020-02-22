import random

print("Hello, what is your name? ")
name = input()

print("Welcome " +name+ " I am thinking of a number between 1 and 10")
guessTaken = 0
number = random.randint(1, 10)

while guessTaken < 6:
    print("Take a guess")
    guess = input()
    guess = int(guess)

    guessTaken+=1
    if guess < number:
        print("Number too low")
    elif guess > number:
        print ("Number too high")
    elif guess == number:
        break
if guess == number:
    guessTaken = str(guessTaken)
    print("Good job "+name+ ", you guessed the number in " +guessTaken+ "trials")
if guess != number:
    number = str(number)
    print("Nope, the number I am thinking of is " +number)
    print(" ")