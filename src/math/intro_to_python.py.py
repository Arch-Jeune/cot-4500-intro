import numpy as np
#Use numpy.eye() function to create idenity matrix
#Print the array where a cell is 1==j, else 0
a = np.eye (3)
print (a)
#Print 3x3 matrix from #1 and then add 3 to every cell where i is not j
print ('\n')
a = np.eye (3)
a[a != 1] += 3
print (a)
#Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created
print ('\n')
a = np.eye (3)
a[a != 1] += 3
a = np.delete (a, -1, 1)
print (a)
