import itertools as it
import timeit





def cross(A,B):
    return [a+b for a in A for b in B]

def crossWL(A,B):
    return [x+y for x,y in it.product(A,B)]







letters = 'ABCDEFGHJHI'
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
