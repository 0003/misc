import itertools as it
import timeit


def cross(A,B):
    return [a+b for a in A for b in B]

def crossWL(A,B):
    return [x+y for x,y in it.product(A,B)]



letters = 'ABCDEFGHI'
digits = '123456789'
rows = letters
cols = digits

squares = cross(rows,cols)
squaresWL = crossWL(rows,cols)

print squares
print squaresWL
print timeit.timeit("cross(rows,cols)",number=1000, setup= "from __main__ import cross, rows, cols")
print timeit.timeit("crossWL(rows,cols)",number=1000, setup= "from __main__ import cross, crossWL, rows, cols")
print len(squares)
#Norvigs cross-product function runs faster.


""" units as defined by norbig are sets of 9 squares.
    peers are all the squares that belong to a unit"""

#
list_of_units = [cross(rows,column_number) for column_number in cols] +\
                 [cross(row_letters,cols) for row_letters in rows] +\
                 [cross(three_row_letters, three_col_letters) for three_row_letters in ['ABC','DEF','GHI']
                 for three_col_letters in ['123','456','789']]


print "printing list of units \n"
for n, l in enumerate(list_of_units):
    print n, l

""" units is a dict that maps a square to all of its units """

units = dict( (square,[unit for unit in list_of_units if square in unit])
               for square in squares)
print '\n printing unit test'
print units['A1']
print len(units['A1'])

"""peers is a dict that maps a square to all of its peer squares """

peers = dict( (square,set(sum(units[square],[])) - set([square])) for square in squares)

print '\n printing peer test'
print peers['A1']
print len(peers['A1'])
print set(sum(units['A1'],[])) - set(['A1'])
print sum(units['A1'],[])


""" Grid is the input that represents the initial state
    Values are the intermediate status of the grid that we will change. This will be a dict with the key
    being a square - ie 'A1' -- and the values being a string of remaining digits - ie '123456'"""

def grid_values(grid):
    """Takes a grid and converts it into values"""
    #0. mean we need to fgure them out.
    characters = [character for character in grid if character in digits or character in '0.']
    return dict(zip(squares,characters))

def eliminate(values, square, digit):
    """Where the magic happens"""


def assign(values, square, digit):
    
    other_values = values[square].replace(digit,'')
    if all(eliminate(values,square,od) for od in other_values):
        return values
    return False

def parse_grid(grid):
    """Parse grid takes a grid input and returns a list of possible values for each square. Otherwise
    it returns FALSE."""
    #Build a dict of squares and digits
    values = dict((s,digits) for square in squares)
    for s, d in grid_values(grid).items():
        #need to make assign
        if d in digits and not assign(values,s,d):
            #
            return False
    return values

print grid_values('00300.')