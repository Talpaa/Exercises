def valid_sudoku_line(linea: list):

    for i in linea:

        if not(i == "."):
        
            count: int = 0

            for j in linea:

                if i == j:

                    count += 1

            if count > 1:

                return False
            
    return True

def valid_sudoku_column(colonna: list):
    
    cifre: list = ['1','2','3','4','5','6','7','8','9']

    for i in colonna:

        if i in cifre:

            cifre.remove(i)

        else: 

            return False
        
    return True

def valid_sudoku_box(box: list):
    
    cifre: list = ['1','2','3','4','5','6','7','8','9']

    for i in box:

        if i in cifre:

            cifre.remove(i)

        else: 

            return False
        
    return True

def valid_sudoku(board: list[list[str]]) -> bool:
    # la tavola del sudo viene rapperentata come una matrice (lista di liste)
    # con 9 righe e 9 colonne
    
    valid: bool = True

    for l in board:

        valid = valid_sudoku_line(l)

        if not(valid):

            return valid
        
    
    for n in range(0,9):

        colonna: list = []

        for c in board:

            if not(c[n] == '.'):
                colonna.append(c[n])

        valid = valid_sudoku_column(colonna)

        if not(valid):

            return valid

    #permette di creare una lista del riquadro in alto a sinistra del sudoku
    box: list = []
    for i in board:

        for n in range(0,3):

            if not(i[n] == '.'):

                box.append(i[n])

        ind: int = (board.index(i))+1
        if (ind % 3) == 0:

            valid = valid_sudoku_box(box)

            if not(valid):

                return valid
            
            box = []

    box: list = []
    for i in board:

        for n in range(3,6):

            if not(i[n] == '.'):

                box.append(i[n])

        ind: int = (board.index(i))+1
        if (ind % 3) == 0:

            valid = valid_sudoku_box(box)

            if not(valid):

                return valid
            
            box = []

    box: list = []
    for i in board:

        for n in range(6,9):

            if not(i[n] == '.'):

                box.append(i[n])

        ind: int = (board.index(i))+1
        if (ind % 3) == 0:

            valid = valid_sudoku_box(box)

            if not(valid):

                return valid
            
            box = []

    return valid


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))#Output True

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))#Output False