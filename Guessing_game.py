from random import randint


for i in range(1,11):
    guessNumber = int(input("Enter your guess value 1 to 10 :"))
    randNumber = randint(1,10)

    if guessNumber == randNumber:
        print("Won the match")

    else:
        print("Loss the game")
        print("Random number was : ",randNumber)