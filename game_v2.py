import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guessing number

    Args:
        number (int, optional): Set number. Defaults to 1.

    Returns:
        int: Amount of tries
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # assumed number
        if number == predict_number:
            break # exit from loop, if number were guessed
    return(count)

print(f'Amount of tries: {random_predict()}')
def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches our algorithm guesses

    Args:
        random_predict ([type]): Guessing function

    Returns:
        int: mean amount of tries
    """

    count_ls = [] # list for saving tries amount
    np.random.seed(1) # receive seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # set list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # calculate mean amount of tries

    print(f'Your algorithm guesses the number on average for: {score} tries')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)