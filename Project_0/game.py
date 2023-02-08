import numpy as np

number = np.random.randint(1, 101) # guessing the number
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100"))

    if predict_number > number:
        print("Number must be lesser!")

    elif predict_number < number:
        print("Number must be greater!")

    else:
        print(f"You guessted it! This number is = {number}, by {count} tries")
        break # End of the game, escape from loop.