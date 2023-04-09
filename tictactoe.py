def print_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def get_player_choice(player, board):
    choice = input(player + ', choose a space to place your marker (1-9): ')
    while not choice.isdigit() or int(choice) not in range(1, 10) or board[int(choice)] != ' ':
        print('Invalid choice. Please choose an empty space between 1 and 9.')
        choice = input(player + ', choose a space to place your marker (1-9): ')
    return int(choice)

def check_win(board):
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    return None

def play_game():
    board = [' '] * 10
    current_player = 'X'
    winner = None

    while not winner:
        print_board(board)
        choice = get_player_choice(current_player, board)
        board[choice] = current_player
        winner = check_win(board)
        if winner:
            print_board(board)
            print('Congratulations, ' + winner + ' wins!')
            break
        if ' ' not in board:
            print_board(board)
            print('It\'s a tie!')
            break
        current_player = 'O' if current_player == 'X' else 'X'

play_game()
