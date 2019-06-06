import random
import tplus

print('Welcome to play Tictactoe!')
while True:
    #choose a letter to play:'X'or'O'
    letter=''
    while not(letter=='X' or letter=='O'):
        print('Please pick one letter to play: X or O?')
        letter =input().upper()
    if letter=='X':
        num_player=1
        num_comp=0
    else:
        num_player=0
        num_comp=1
    #"Flip a coin" to see who will move first
    print('\n......\n......\nLet\'s flip a coin to see who will go first...\n------>')
    if random.randint(0,1)==num_comp:
        turn='computer'
    else:
        turn='player'
    print('The', turn, 'will go first.\n')
    print("\n(Example:If you want to move to row 1,column 2,input 12.)")

    #Before every game, reset the board
    #Store the board value in nested lists.If the space is empty, the value=-3;if letter'X' is in the space,the value=1;if letter 'O' is in the space, the value=0.
    Board=list()
    Board_draw=list()

    Row1=[-3,-3,-3]
    Row2=[-3,-3,-3]
    Row3=[-3,-3,-3]
    Board=[Row1,Row2,Row3]

    '''
    Row1=[-5,-5,-5,-5,-5]
    Row2=[-5,-5,-5,-5,-5]
    Row3=[-5,-5,-5,-5,-5]
    Row4=[-5,-5,-5,-5,-5]
    Row5=[-5,-5,-5,-5,-5]
    Board=[Row1,Row2,Row3,Row4,Row5]
    '''

    #a sign to indicate the game is going on or not
    gamegoing=True
    #In a single game
    while gamegoing:
        #when it's the player's turn to move
        if turn=='player':
            #draw the board and get the player's input
            Board_draw = tplus.mapboard(Board)
            tplus.drawboard(Board_draw)
            (row_index,col_index)=tplus.getplayermove(Board)

            #check if the player won
            if tplus.checkwin(Board,row_index,col_index,num_player):
                Board[row_index][col_index]=num_player
                Board_draw = tplus.mapboard(Board)
                tplus.drawboard(Board_draw)
                print("\n***Congratulations!You Win!***")
                gamegoing=False

            else:
                Board[row_index][col_index]=num_player
                empty_p=list()
                empty_p=tplus.checkempty(Board)
                #check if the board is full now
                if len(empty_p)<1:
                    Board_draw = tplus.mapboard(Board)
                    tplus.drawboard(Board_draw)
                    print("\n===The Game is a tie!===")
                    gamegoing=False

                else:
                    turn='computer'

        #when it's the computer's turn to move
        else:
            empty_c=list()
            empty_c=tplus.checkempty(Board)
            #first:check if it's the last empty space left in the game.
            if len(empty_c)==1:
                row_index=empty_c[0][0]
                col_index=empty_c[0][1]
                win_sign=tplus.checkwin(Board,row_index,col_index,num_comp)
                Board[row_index][col_index]=num_comp
                Board_draw = tplus.mapboard(Board)
                tplus.drawboard(Board_draw)
                if win_sign:
                    print("\n~~~Computer Win!~~~")
                else:
                    print("\n===The Game is a tie!===")
                gamegoing=False

            else:
                #second:check if computer can win in the next move.
                for (r,c) in empty_c:
                    if tplus.checkwin(Board,r,c,num_comp):
                        Board[r][c]=num_comp
                        Board_draw = tplus.mapboard(Board)
                        tplus.drawboard(Board_draw)
                        print("\n~~~Computer Win~~~")
                        gamegoing=False
                        break

                #third: find the player's lead-to-win-move and take it
                for (r,c) in empty_c:
                    if tplus.checkwin(Board,r,c,num_player):
                        Board[r][c]=num_comp
                        turn='player'
                        break

                #fourth: if none of above can be found, just randomly pick one empty space
                if turn=='computer':
                    random_index=tuple()
                    random_index=random.choice(empty_c)
                    row_index=random_index[0]
                    col_index=random_index[1]
                    Board[row_index][col_index]=num_comp
                    turn='player'

    print("\nWould you like to play again?(Please enter yes or no)")
    if not input().lower().startswith('y'):
        break
