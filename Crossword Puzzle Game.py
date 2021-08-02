board=[[' ']*20 for i in range (20)]

def printboard(board):
    print('--------------------------------------------------')
    for x in range(len(board)) :
        for y in range(len(board[x])) :
            print(board[x][y], end = '')
        print()
    print('--------------------------------------------------')


def addFirstWord(board, word):
    if len(word) <= len(board):                                                 # check if word can fit into the board
        a,b = len(board),len(board[2])                                          # a=length of row; b=length of col
        targeta = int(a / 2)                                                    # middle row of the matrix
        targetb = int( (b-len(word)) / 2 )                                      # the position to start to put the word in

        for i in word:
            board[targeta][targetb] = i
            targetb += 1


def checkvertical(board, word, row, col):
    if len(word) + row <= 20:                                                   # check if the word can fit into the board
        for i in range (len(word)):
            boardletter = board[row+i][col]                                     # starting from [row,col] and end by [row+len(word),col]
            
            if word[i] == boardletter:                                          # intersect and match at least one non-blank letters on the board
                
                ''' check the perimeter of the word to ensure that it won't create any new word'''
                # check the left and right col:
                for a in range (len(word)):
                    boardletter_left = board[row + a][col - 1]
                    boardletter_right = board[row + a][col + 1]
                    if boardletter_left != ' ' or boardletter_right != ' ':
                        if a != i:
                            return False

                # check the head and tail:
                if board[row-1][col] != ' ' or board[row+len(word)][col] != ' ':
                    return False

                # check if it's going to change any existing words:
                for b in range (len(word)):
                    if board[row+b][col] != ' ' and board[row+b][col] != word[i]:
                        return False

                return True

            elif boardletter==' ': continue                                     # if blank: continue
                
            elif boardletter != word[i]: return False                           # no match to existing letters
                
    return False


def addveretical(board,word):                                                   # start checking from left-top corner to right-bottom
    for a in range(20):
        for b in range(20):
            if checkvertical(board,word,b,a):                                   # find if there is a right position to put in the word
                for i in range(len(word)):                                      # adding words by replacing ' ' to word[i]
                    board[b+i][a] = word[i]
                
                return True
    
    return False


def checkhorizontal(board,word,row,col):
    if len(word)+col <= len(board):                                             # check if the word can fit into the board
        for i in range (len(word)):
            boardletter=board[row][col+i]                                       # starting from [row,col] and end by [row+len(word),col]
            
            if word[i] == boardletter:                                          # intersect and match at least one non-blank letters on the board
                
                '''check the perimeter of the word to ensure that it won't create any new word'''

                # check the up and down row:
                for a in range (len(word)):
                    boardletter_up = board[row-1][col+a]
                    boardletter_down = board[row+1][col+a]
                    
                    if boardletter_up != ' ' or boardletter_down != ' ':
                        if a != i:
                            return False

                # check the head and tail:
                if board[row][col-1] != ' ' or board[row][col+len(word)] != ' ': return False

                # check if it's going to change any existing words:
                for b in range(len(word)):
                    if board[row][col+b] != ' ' and board[row][col+b] != word[i]:
                        return False

                return True
            
            elif boardletter==' ': continue                                     # if blank: continue
                
            elif boardletter != word[i]:  return False                          # no match to existing letters
               
    return False


def addhorizontal(board,word):                                                  # start checking from left-top corner to right-bottom
    for a in range(len(board)):
        for b in range(len(board)):
            if checkhorizontal(board,word,a,b):
                for i in range(len(word)):                                      # adding words by replacing ' ' to word[i]
                    board[a][b+i] = word[i]
                return True
    
    return False


def crossword(L):
    board = [[' '] * 20 for i in range(20)]
    addFirstWord(board,L[0])                                                    # add first word to the center first
    
    for i in range (1,len(L)):
        if i % 2 == 0:  addhorizontal(board,L[i])
        else:           addveretical(board,L[i])
    
    printboard(board)                                                           # print the final board


crossword(['addle', 'apple', 'clowning', 'incline', 'plan', 'burr'])
crossword(['ARCHETYPE','AUTHORITY','BENCHMARK','CRITERION','EXEMPLIFY','PRECEDENT','PROTOTYPE','QUOTATION','REFERENCE','ROLEMODEL','ULTIMATUM]'])