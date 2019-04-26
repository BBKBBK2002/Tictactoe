def mapboard(board):
    '''list of numbers->list of strings
    mapping a list of numbers to a list of strings.
    Mapping Rules: 1->'X',0->'O',otherwise->' '.
    '''
    board_after=[]
    for Row in board:
        Row_after=[]
        for col in Row:
            if col==1:
                Row_after.append('X')
            elif col==0:
                Row_after.append('O')
            else:
                Row_after.append(' ')
        board_after.append(Row_after)

    return board_after



def drawboard(board_todraw):
    '''(nested list)->None
    Input a nested list of elements(matrix), the function will draw the board and put the elements to the corresponding space.
    Condition: Please input a square matrix.
    '''
    N= len(board_todraw)
    for rownum in range(N):
        rownum1=N-rownum
        print(rownum1,'  ',end='')
        for colnum in range(N):
            print('|',board_todraw[rownum1-1][colnum],end='')
        print('')

        print('----',end='')
        for colnum in range(N):
            print('+--',end='')
        print('')

    print('R ','C',end='')
    for colnum in range(N):
        print('|',colnum+1,end='')





def getplayermove(board):
    ''' To get the input move number of the player
    '''
    N=len(board)
    goodinput_sign=False
    while goodinput_sign==False:
        player_move=input("\nNow please enter a number to move: ")
        move=int(player_move)
        row_index=move//10-1
        col_index=move%10-1
        if row_index in range(N) and col_index in range(N) and (board[row_index][col_index]<0):
            goodinput_sign=True
        else:
            print('The input is wrong: either the number is out of range or the space is full.')
    return (row_index,col_index)



def checkwin(board,rowindex,colindex,move_num):
    '''(nested list, int,int)->bool
        Given the board(before the move) and the move, check/predict if the move will lead to win or not.
        Condition: rowindex and colindex count from 0.
    '''
    N=len(board)
    sign=(N-1)*move_num-N

    #check the row
    sumrow=sum(board[rowindex])
    if sumrow==sign:
        return True
    #check the column
    sumcol=0
    for Row in board:
        sumcol=sumcol+Row[colindex]
    if sumcol==sign:
        return True
    #if the element is on the diagonal, check the line.
    if rowindex==colindex:
        sumdiag1=0
        for i in range(N):
            sumdiag1=sumdiag1+board[i][i]
        if sumdiag1==sign:
            return True
    #Another case of diagonal
    if(rowindex+colindex)==N-1:
        sumdiag2=0
        for i in range(N):
            sumdiag2=sumdiag2+board[i][N-1-i]
        if sumdiag2==sign:
            return True
    return False



def checkempty(board):
    '''(nested list)->(nested list)
        to find the empty space on the board. Return a list of all the empty space.
    '''
    N=len(board)
    emptyspace=[]
    for row in range(N):
        for col in range(N):
            if board[row][col]<0:
                emptyspace.append((row,col))
    return emptyspace
