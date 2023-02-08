import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Initially we set random number, then icrease or reduce it in depend on
    whether it is more or less than the set number.
       
       The function takes the set number and returns amount of tries
           
    Args:
        number (int, optional): The set number. Defaults to 1.

    Returns:
        int: Amount of tries
    """
    count = 0
    max_number = 100
    min_number = 0
    predict_number = np.random.randint(1, 101)  # generated number

    while True:
        count += 1

        if predict_number > number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2

        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2

        else:
            break  # end of the game, exit from the cycle

    return count

def score_game(random_predict) -> int:
    """Mean amount of tries which algorithm takes to guess the set number 
    at 1000 approaches  
    
    Args:
        random_predict ([type]): Guessing function

    Returns:
        int: mean amount of tries
    """
    count_ls = []
    np.random.seed(1)  # fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  
    # set list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number in: {score} tries")

#Run
if __name__ == '__main__':
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)