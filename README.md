# tic-tac-toe-A.I.
This a is tic-tac-toe A.I. python program ,submitted by Chandermohan, S.A.P. I.D. 500075824, Roll No=63.
There are several different functions in this program, 
1) insertletter is used to take input at a specific position
2)spaceisfree is checking for free space in the board
3)winner function here contains some conditions for winning
4)playermove here takes player's input for next move
5)compmove is responsible for the next move of computer
6)boardfull is use to check for any available free space
7)printboard is use to print the board of tic tac
In main function we are asking for the player to play game,after taking input yes the program will run and ask for a position to place'x'
now the 'compmove' function will check for all possible place to put 0,now again it will ask for input from user and so on.Here the 'compmove' function will check for corner moves and edge moves seperately for pc, and will use its next move in available spaces in corner and edges.Now if the moves are less than 1 ,it will print game is tie, for either pc or player if condition of 'winner' function is true winner will be declared
