board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

    
def Winner(o, e): # here we define a function which contains some conditions ,for a winner(either pc or player) one of the given condition must be followed. 
    return (o[7] == e and o[8] == e and o[9] == e) or (o[4] == e and o[5] == e and o[6] == e) or(o[1] == e and o[2] == e and o[3] == e) or(o[1] == e and o[4] == e and o[7] == e)or(o[2] == e and o[5] == e and o[8] == e) or(o[3] == e and o[6] == e and o[9] == e) or(o[1] == e and o[5] == e and o[9] == e) or(o[3] == e and o[5] == e and o[7] == e)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for y in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = y
            if Winner(boardCopy, y):
                move = i
                return move

    cornermoves = []  # here we created a list 'cornermoves',now we are checking for available moves at [1,3,5,7] in list 'possiblemoves' if the moves are present we are appending them in list cornermoves 
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornermoves.append(i)
            
    if len(cornermoves) > 0:     # if there are moves available at corner, we are using 'selectRandom' function to select a move from cornermoves
        move = selectRandom(cornermoves)
        return move

    if 5 in possibleMoves:        #here we are checking if there is a move present a 5th place or middle place
        move = 5
        return move

    edgemoves = []         # here we are checking for moves at edges same as corner moves
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgemoves.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgemoves)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def BoardFull(board): # here we define a function name BoardFull with argument board( which we defined at the top of program),now here this function is checking for any free space
    if board.count(' ') > 1:
        return False
    else:
        return True


def printBoard(board): # we define this function to print the board
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)                 # here we are priting the empty board on screen

    while not(BoardFull(board)):
        if (Winner(board, 'O')):
            print('P.C. won this time!')
            break
        else:
            playerMove()
            printBoard(board)

        if (Winner(board, 'X')):
            print('you won this time! Good Job!')
            break
        else:
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)


            

    if BoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
