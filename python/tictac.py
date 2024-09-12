#
#  Nome do arquivo: EvenFibonacciNumbers.py
#  Descrição: Programa de uma possível solução para simular o jogo Tic Tac Toe (em fase de testes)
#  Autor: Ana Paula da Silva Souza
#  Data: 09/2024
#  Versão: 1.0
#  Licença: Apache
#
import random
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for line in board:
        print('+-------'*3,'+', sep="")
        print('|       '*3,'|', sep="")
        print('|', end="")
        for col in line:
            print('  ',col,'  |', end="")
        print()
        print('|       '*3,'|', sep="")
    print('+-------'*3,'+', sep="")

def line_col(move):
     # identifying column of board
    col = -1
    if move in [3,6,9]:
        col = 2
    elif move in [2,5,8]:
        col = 1
    else:
        col = 0
    
    # identifyin line of board
    line = -1
    if move in [1,2,3]:
        line = 0
    elif move in [4,5,6]:
        line = 1
    else:
        move = 2
    return [line, col]

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    moves = 0
    
    while True:
        display_board(board)
        if moves > 8:
            print("Draw! :-|")
            break
        move = int(input("What's your move?\n"))
        if move < 1 and move > 9:
            print('Not permited!')
            continue

        lista = line_col(move)
        line = lista[0]
        col = lista[1]

        if type(board[line][col]) == int:
            board[line][col] = 'O'
        else:
            print("You can't do it!")
            moves -= 1
            continue
        moves += 1
        draw_move(board)
        if moves > 3 and victory_for(board, 'O') == 'O':
            display_board(board)
            print('You win!! :-)')
            break
        if moves > 8:
            display_board(board)
            print("Draw! :-|")
            break
        moves += 1
        if moves > 3 and victory_for(board, 'X') == 'X':
            display_board(board)
            print('You lose! :-(')
            break
        
        print(moves)

def make_list_of_free_fields():
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return [[1,2,3],[4,5,6],[7,8,9]]

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    o = None
    x = None
    xd = True
    od = True
    for i in range(3):
        x = True
        o = True
        for j in range(3):
            if board[i][j] != 'O':
                o = False
            if board[i][j] != 'X':
                x = False
        if o:
            return 'O'
        if x:
            return 'X'
            
        for j in range(3):
            if board[j][i] != 'O':
                o = False
            if board[j][i] != 'X':
                x = False
        if o:
            return 'O'
        if x:
            return 'X'
        
            
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return 'O'
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return 'X'
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return 'O'
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return 'X'
    

def draw_move(board):
    while True:
        move = random.randrange(1,9)
        lista = line_col(move)
        line = lista[0]
        col = lista[1]
        # identifyin line of board
        if type(board[line][col]) == int:
            board[line][col] = 'X'
            break
    
    # The function draws the computer's move and updates the board.

enter_move(make_list_of_free_fields())