from random import randint

secret = randint(1, 20)
a = int(input("From 1 to 20, guess which is the secret number? "))

if secret == a:
    print("Congrats! ", secret, " is the secret number. You won!")
else:
    print("Wrong,", a , "is not the secret number.")
