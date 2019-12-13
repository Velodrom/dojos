Implement a function that finds any of the equilibrium indices of an array A.

Equilibrium index of an array A of length N is defined as the number P
(0 <= P < N) such that the sum of all elements before P equal to the sum of
elements after P, i.e.

A[0] + A[1] + ... + A[P-1] = A[P+1] + ... + A[N-2] + A[N-1]

Sum of zero elements is assumed to equal to 0, which can happen if
P = 0 or P = N-1. The function should return -1 if no equilibrium
index exists.

============

Example:

For an array A with N = 5 and the following elements:

A[0] = 2
A[1] = -3
A[2] = 4
A[3] = -2
A[4] = 1

P = 0 is an equilibrium index because there are no elements before A[0], and
A[] = 0 = A[1] + A[2] + A[3] + A[4]

P = 2 is an equilibrium index because
A[0] + A[1] = -1 = A[3] + A[4]
