a = 7

while True:
    guess = int(input("Guess number a: "))

    if guess == a:
        print("Correct")
        break

    print("Wrong")