import random
print("Hi welcome to the game, This is a number guessing game.\nLet's start the game")
n=random.randrange(1,100)
guess=int(input("Enter a number:"))
while n != guess:
    if guess < n:
        print("Too Low!")
        guess=int(input("Enter a number again:"))
    elif guess > n:
        print("Too High!")
        guess=int(input("Enter a number again:"))
    else:
        break
print("Woww , You got it correct !!")
