import random
import queue

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_game_over():
    if (board[0] == board[1] == board[2] != "-") or \
       (board[3] == board[4] == board[5] != "-") or \
       (board[6] == board[7] == board[8] != "-") or \
       (board[0] == board[3] == board[6] != "-") or \
       (board[1] == board[4] == board[7] != "-") or \
       (board[2] == board[5] == board[8] != "-") or \
       (board[0] == board[4] == board[8] != "-") or \
       (board[2] == board[4] == board[6] != "-"):
        return "win"
    elif "-" not in board:
        return "tie"
    else:
        return "play"

def bfs_ai_move(player):
    q = queue.Queue()
    q.put((board.copy(), None))  

    while not q.empty():
        current_board, move = q.get()

        
        if check_winner(current_board, player):
            return move

        
        for i in range(9):
            if current_board[i] == "-":
                new_board = current_board.copy()
                new_board[i] = player
                q.put((new_board, i))

    
    return [i for i in range(9) if board[i] == "-"][0]

def check_winner(board_state, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]            
    ]
    return any(all(board_state[pos] == player for pos in condition) for condition in win_conditions)

def random_agent_move():
    available_positions = [i for i, mark in enumerate(board) if mark == "-"]
    return random.choice(available_positions)

def take_turn(player):
    print(player + "'s turn.")
    if player == "X":  
        position = bfs_ai_move(player)
    else:  
        position = random_agent_move()

    board[position] = player
    print_board()

def play_game():
    print_board()
    current_player = "X"
    game_over = False
    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

play_game()
