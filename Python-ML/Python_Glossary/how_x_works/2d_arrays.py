'''
an abstracted example of a 9x9 2D array
'''

def twoDArray(f, s):
    for i in range(9):
        print(i)
        if i == 1:
            f = 0
        elif i == 2:
            f = 0
        elif i == 3:
            f = 3
        elif i == 4:
            f = 3          
        elif i == 5:          
            f = 3
        elif i == 6:          
            f = 6
        elif i == 7:          
            f = 6
        elif i == 8:          
            f = 6
        for j in range(3):
            #s = 0
            if i == 1:
                s = 3
            elif i == 2:
                s = 6
            elif i == 3:
                s = 0
            elif i == 4:
                s = 3
            elif i == 5:          
                s = 6
            elif i == 6:          
                s = 0
            elif i == 7:          
                s = 3
            elif i == 8:          
                s = 6
            for k in range(3):
                n = i
                print(f"iteration {n}: [{f}][{s}]")
                n += 1
                s += 1
            f += 1        
    print("Assume a 9x9 grid. for each i, the indeces" +
          " of all nine 3x3 sub-grids are printed")

#begin at the upper-most left side of grid
twoDArray(0,0)