import random


# Player move function
def player_move(move, sticks, max_sticks):
    if move < 1 or move > min(sticks, max_sticks):  # Check if move is valid
        print("Invalid move")
        move = int(input("Enter your move: "))
        return player_move(move, sticks, max_sticks)
    else:
        return move  # Return how many sticks the player takes

# MAX-Value function
def max_value(sticks, alpha, beta, max_sticks):
    if sticks <= 0:
        return -1
    value = -1
    for move in range(1, min(sticks,max_sticks)+1):
        v = min_value(sticks - move, alpha, beta, max_sticks)
        value = max(value, v)
        if value >= beta:
            return value
        alpha = max(alpha, value)

    return value


# MIN-Value function
def min_value(sticks, alpha, beta, max_sticks):
    if sticks <= 0:
        return 1
    value = 1
    for move in range(1, min(sticks, max_sticks) + 1):
        v = max_value(sticks - move, alpha, beta, max_sticks)
        value = min(value, v)
        if value <= alpha:
            return value
        beta = min(value, beta)

    return value


# Computer move function
# def computer_move(sticks, max_sticks):
#     best_move = None
#     alpha = -1
#     beta = 1
#     value = -1
#     for move in range(1, min(sticks, max_sticks) + 1):
#         v = min_value(sticks - move, alpha, beta, max_sticks)
#         value = max(v, value)
#         if value > alpha:
#             alpha = value
#             best_move = move
#     return best_move


def computer_move(sticks, max_sticks):
    best_move = None
    alpha = -1
    beta = 1
    value = -1
    for move in range(1, min(sticks, max_sticks) + 1):
        v = min_value(sticks - move, alpha, beta, max_sticks)
        if v > value:
            value = v
            best_move = move
        if value >= beta:
            return best_move
        alpha = max(alpha, value)

    if best_move is None:
        best_move = random.randint(1,min(sticks, max_sticks))
        return best_move
    else:
        return best_move


def nim():
    max_sticks = int(input(
        "Enter the maximum number of sticks each player can take: "))  # Input for maximum number of sticks each player can take
    sticks = int(input("How many sticks do you want to play with? "))  # Input for number of sticks to play with
    print('|' * sticks)
    print(f"There are {sticks} sticks left")

    while sticks > 0:
        c_move = computer_move(sticks, max_sticks)
        print(f"The computer takes {c_move} sticks")
        sticks -= c_move
        print('|' * sticks)
        print(f"There are {sticks} sticks left")
        if sticks == 0:  # Check if computer has won
            print("Computer wins!")
            break
        player_input = int(input("Enter how many sticks you want to take: "))
        p_move = player_move(player_input, sticks, max_sticks)
        sticks -= p_move
        print('|' * sticks)
        print(f"There are {sticks} sticks left")
        if sticks == 0:  # Check if player has won
            print("You Win!")
            break


nim()
