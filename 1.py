# Name: Xinyu Zhang

# Main function   
def main():
    board = list("012345678")
    player1 = "X"
    player2 = "O"

    while True:
        print_board(board)
        move1 = player_1(board)
        board[move1] = player1

        if win(board):
            print_board(board)
            print ("Player 01 win!")
            break

        if draw(board):
            print_board(board)
            print("Draw!")
            break

        print_board(board)
        move2 = player_2(board)
        board[move2] = player2

        if win(board):
            print_board(board)
            print ("Player 02 win!")
            break

        if draw(board):
            print_board(board)
            print("Draw!")
            break

# Create a board
def print_board(board):
    print("{0}|{1}|{2}".format(board[0],board[1],board[2]))
    print('-+-+-')
    print("{0}|{1}|{2}".format(board[3],board[4],board[5]))
    print('-+-+-')
    print("{0}|{1}|{2}".format(board[6],board[7],board[8]))

# Define legal moves
def moves(board):
    moves = []
    for i in range(9):
        if board[i] in list("0123456798"):
            moves.append(i)
    return moves

# First player input moves
def player_1(board):
    move = 9
    while move not in moves(board):
        move = int(input("Enter your move player 01 (X): "))
    return move

# Second Player input moves
def player_2(board):
    move = 9
    while move not in moves(board):
        move = int(input("Enter your move player 02 (O): "))
    return move

# There are 8 ways to win.
def win(board):
    set_win = {(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)}
    for i in set_win:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return True
    return False

# If the board is fiied, then draw. 
def draw(board):
    for i in list("012345678"):
        if i in board:
            return False
    return True


main()
