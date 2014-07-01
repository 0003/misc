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

