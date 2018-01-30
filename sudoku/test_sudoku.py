from sys import argv

from sudoku import Sudoku


if __name__ == '__main__':
    grille1 = [[ 9 ,'-','-','-','-','-','-','-', 2],
               [ 3 ,'-', 7 , 1 ,'-','-', 4 ,'-', 8],
               ['-', 1 ,'-','-', 5 , 4 ,'-', 6 ,'-'],
               ['-','-', 1 ,'-','-','-','-', 7 ,'-'],
               ['-','-', 4 ,'-','-','-', 9 ,'-','-'],
               ['-', 2 ,'-','-','-','-', 8 ,'-','-'],
               ['-', 8 ,'-', 3 , 2 ,'-','-', 4 ,'-'],
               [ 7 ,'-', 3 ,'-','-', 6 , 2 ,'-', 1],
               [ 4 ,'-','-','-','-','-','-','-', 5]]

    grille2 = [['-','-','-','-','-','-','-','-','-'],
               ['-','-', 7 , 8 , 3 ,'-', 9 ,'-','-'],
               ['-','-', 5 ,'-','-', 2 , 6 , 4 ,'-'],
               ['-','-', 2 , 6 ,'-','-','-', 7 ,'-'],
               ['-', 4 ,'-','-','-','-','-', 8 ,'-'],
               ['-', 6 ,'-','-','-', 3 , 2 ,'-','-'],
               ['-', 2 , 8 , 4 ,'-','-', 5 ,'-','-'],
               ['-','-','-','-', 9 , 6 , 1 ,'-','-'],
               ['-','-','-','-','-','-','-','-','-']]


    if len(argv) > 1 and argv[1] == '2':
        s = Sudoku(grille2)
    else:
        s = Sudoku(grille1)

    print(s)
    s.resoudre() # forward checking
    s.resoudre('backtracking')
    print(s)