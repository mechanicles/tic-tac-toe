#----------------------------------------------
# TicTacToe game in Python
# author: [Sanosh Wadghule, santosh.wadghule@gmail.com]
# copyright: (c) 2010-2011 Santosh Wadghule
#----------------------------------------------

import sys
import random
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

print "--------------------------"
print "Powerful TicTacToe Game"
print "--------------------------"
print 

def displayPos():
    print "Postion of board: "
    print "0 | 1 | 2"
    print "3 | 4 | 5"
    print "6 | 7 | 8"

player = random.randrange(1, 3)     #choose random player

def displayBoard(board):
    print "========="
    print board[0] + " | " + board[1] + " | " + board[2]
    print board[3] + " | " + board[4] + " | " + board[5]
    print board[6] + " | " + board[7] + " | " + board[8]
    print "========="

def checkwin(a,b,c,player,board):
    if board[a] == 'X' and board[b] == 'X' and board[c] == 'X':
        print       #newline
        print "Player - " + str(player) + " is *** WINNER ***!!!"
        displayBoard(board)
        sys.exit()
    
    elif board[a] == 'O' and board[b] == 'O' and board[c] == 'O':
        print   #newline
        print "Machine is *** WINNER ***!!!"
        displayBoard(board)
        sys.exit()


def winner(board,player):
    checkwin(0,1,2,player,board)
    checkwin(3,4,5,player,board)
    checkwin(6,7,8,player,board)
    checkwin(0,3,6,player,board)
    checkwin(1,4,7,player,board)
    checkwin(2,5,8,player,board)
    checkwin(0,4,8,player,board)
    checkwin(2,4,6,player,board)


def play(board,x,player):
    if board[x] != ' ':
        print "--You have chosen wrong position--"
        sys.exit()
    else:
        if player == 1:
            board[x] = 'X'
            winner(board,player)
        else:
            board[x] = 'O'
            winner(board,player)


def checkPriority(a,b,c,board):
    if (board[a] == 'X' and board[b] == 'X') or (board[a] == 'O' and board[b] == 'O'):
	if board[c] == ' ':
	    return c
    elif (board[a] == 'X' and board[c] == 'X') or (board[a] == 'O' and board[c] == 'O'):
    	if board[b] == ' ':
            return b
    elif (board[b] == 'X' and board[c] == 'X') or (board[b] == 'O' and board[c] == 'O'):
    	if board[a] == ' ':
           return a
                 

def Priority(board):
	y = checkPriority(0,1,2,board)
	if y == None:
	    y = checkPriority(3,4,5,board)
	if y == None:	
	    y = checkPriority(6,7,8,board)
	if y == None:
	    y = checkPriority(0,3,6,board)
	if y == None:
	    y = checkPriority(1,4,7,board)
	if y == None:
	    y = checkPriority(2,5,8,board)
	if y == None:
	    y = checkPriority(0,4,8,board)
	if y == None:
	    y = checkPriority(2,4,6,board)
	
	if y != None:
	    return y
	else:
	    while True:
	        x = random.randrange(0, 9)
		if board[x] != 'X' and board[x] != 'O':
		    break
		else:
		    continue
        return x

for i in range(0,9):
    if player == 1:
        print "Player " + str(player) + " >> Its your turn"
        displayPos()
        x = input("--Enter the position number: ")
        play(board,x,player)
        displayBoard(board)
        print       #newline
        player = 2
    else:
        print "Machine >> Its your turn"
        displayPos()
        if i == 0:
	    x = random.randrange(0, 9)
	    if board[x] != 'X' and board[x] != 'O':
	        play(board,x,player)
        
        else:
	    x = Priority(board)
	    play(board,x,player)
        
        displayBoard(board)
        print       #newline
        player = 1


print "--Match Draw--"