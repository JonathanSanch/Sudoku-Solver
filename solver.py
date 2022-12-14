#project to learn the backtracking algorithm and practice meaningful comments

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#recursively backtrack through the board
def solve(bo):
    
    find = find_empty(bo)
    if not find:
        return True
    else: 
        row, col = find

#Function checks if the given board, number, and starting position are valid
def valid(bo, num, pos):
    
    #Check Row
    for i in range(len(bo[0])):
        #pos[0] is the row position of the tuple (i, j) and i is the column position of loop
        if bo[pos[0]][i] == num and pos[1] != i: #going to ignore checking if the position is the same as insert postion
            return False #2 of the same number in one row
    
    #Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #Check box 
    box_x = pos[1] // 3 #integer divsion by 3 gives location of box
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3): #range of the beginning to the end of box
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and pos != (i, j): #if the box already contains value and box is not empty
                return False
    
    return True

#Print Sudoku Board To Screen
def print_board(bo):
    
    #Creates board structure using "-" and "|"
    for i in range(len(bo)):
        
        #Creates Row Seperation
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        
        #Creates Column Seperation
        for j in range(len(bo[0])):
            #Prints a column on every 3rd number excluding the first
            if j % 3 == 0 and j != 0:
                #end= prevents print function from going to next line
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                #format last index to string to append space
                print (str(bo[i][j]) + " ", end="")

#given a sudoku board, finds the first empty square. (Denoted by 0)
def find_empty(bo):
    
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
            
    return None

print_board(board)
