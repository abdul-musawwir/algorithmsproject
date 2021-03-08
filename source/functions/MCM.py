# Function to find the most efficient way to multiply
# given sequence of matrices
def MatrixChainMultiplication(dims, i, j, T):
    # base case: one matrix
    if j <= i + 1:
        return 0

    # stores minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix M[i+1]...M[j] = M[i..j]
    min = float('inf')

    # if sub-problem is seen for the first time, solve it and
    # store its result in a lookup table
    if T[i][j] == 0:

        # take the minimum over each possible position at which the
        # sequence of matrices can be split

        """
            (M[i+1]) x (M[i+2]..................M[j])
            (M[i+1]M[i+2]) x (M[i+3.............M[j])
            ...
            ...
            (M[i+1]M[i+2]............M[j-1]) x (M[j])
        """

        for k in range(i + 1, j):

            # recur for M[i+1]..M[k] to get an i x k matrix
            cost = MatrixChainMultiplication(dims, i, k, T)

            # recur for M[k+1]..M[j] to get a k x j matrix
            cost += MatrixChainMultiplication(dims, k, j, T)

            # cost to multiply two (i x k) and (k x j) matrix
            cost += dims[i] * dims[k] * dims[j]

            if cost < min:
                min = cost

        T[i][j] = min

    # return min cost to multiply M[j+1]..M[j]
    return T[i][j]


# if __name__ == '__main__':
#     # Matrix M[i] has dimension dims[i-1] x dims[i] for i = 1..n
#     # input is 10 x 30 matrix, 30 x 5 matrix, 5 x 60 matrix
#     dims = [10, 30, 5, 60]
#
#     # lookup table to store the solution to already computed sub-problems
#     T = [[0 for x in range(len(dims))] for y in range(len(dims))]
#
#     print("Minimum cost is", MatrixChainMultiplication(dims, 0, len(dims) - 1, T))