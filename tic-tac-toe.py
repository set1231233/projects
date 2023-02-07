game_board = ['1','2','3','4','5','6','7','8','9']
original_board = ['1','2','3','4','5','6','7','8','9']

player1 = ''
player2 = ''

isFull = False
game_on = True
winner = False

def display_board(board):
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])

def player_input():
    global player1
    global player2
    while player1 != 'X' or player1 != 'O':
        player1 = input("Which do you want to be? (X or O): ")
        player1 = player1.upper()
        if player1 == 'X':
            print("Player 1 has chosen X.")
            player1 = 'X'
            player2 = 'O'
            break
        elif player1 == 'O':
            print("Player 1 has chosen O.")
            player1 = 'O'
            player2 = 'X'
            break
    return player1


def place_marker(board, player, position):

    board[position-1] = player

    return board[position-1]

def win_check(board):
    global player1
    global player2
    global game_on
    global winner

    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

def space_check(board, position):
    isTaken = False
    if board[position - 1] == 'X' or board[position - 1] == 'O':
        print("That position is already taken choose again.")
        isTaken = True
    else:
        pass
    return isTaken

def full_board_check(board):
    global isFull
    global original_board

    for num in range(9):
        if board[num] == original_board[num]:
            return isFull
    else:
        isFull = True
    return isFull

def player_choice(board):
    good = False
    while good == False:
        choice = int(input("Choose a spot: "))
        space_check(board, choice)
        if space_check(board, choice) == False:
            good = True
            return choice
    return choice

def replay():
    global game_board
    global player1
    global player2
    global isFull
    global game_on

    keep_playing = True

    while keep_playing == True:
        replay = input("Do you want to replay? (Y or N): ")
        replay = replay.upper()
        if replay == 'Y':
            game_board = ['1','2','3','4','5','6','7','8','9']
            player1 = ''
            player2 = ''
            game_on = True
            isFull = False
        elif replay == 'N':
            keep_playing = False
            print("Thanks for playing!")

print("Welcome to Tic Tac Toe!")
while isFull == False:
    display_board(game_board)
    player_input()
    while game_on:

        full_board_check(game_board)
        if isFull == True and winner == False:
            print("The game is a tie!")
            game_on = False
            break
        if game_on:
            print("Player 1's turn.")
            place_marker(game_board, player1, player_choice(game_board))
            display_board(game_board)
            win_check(game_board)

        full_board_check(game_board)
        if isFull == True and winner == False:
            print("The game is a tie!")
            game_on = False
            break
        if game_on:
            print("Player 2's turn.")
            place_marker(game_board, player2, player_choice(game_board))
            display_board(game_board)
            win_check(game_board)

    break
