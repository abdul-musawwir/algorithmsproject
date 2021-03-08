# Function to return a SCS of substrings X[0..m-1], Y[0..n-1]
def SCS(X, Y, m, n, T):
    # if we have reached the end of first string,
    # return second string
    if m == 0:
        return Y[:n]

    # if we have reached the end of second string,
    # return first string
    if n == 0:
        return X[:m]

    # if last character of X and Y matches, then include it in SSC
    # and recur to find SCS of substring X[0..m-2], Y[0..n-1]
    if X[m - 1] == Y[n - 1]:
        return SCS(X, Y, m - 1, n - 1, T) + X[m - 1]
    else:
        # if the last character of X and Y don't match

        # if top cell of current cell has less value than the left
        # cell, then include current character of X in SCS
        # and find SCS of substring X[0..m-2], Y[0..n-2]

        if T[m - 1][n] < T[m][n - 1]:
            return SCS(X, Y, m - 1, n, T) + X[m - 1]

        # if left cell of current cell has less value than the top
        # cell, then include current character of Y in SCS
        # and find SCS of substring X[0..m-1], Y[0..n-2]
        else:
            return SCS(X, Y, m, n - 1, T) + Y[n - 1]


# Function to fill lookup table by finding length of SCS of
# sequences X[0..m-1] and Y[0..n-1]
def SCSLength(X, Y, m, n, T):
    # initialize first column of the lookup table
    for i in range(m + 1):
        T[i][0] = i

    # initialize first row of the lookup table
    for j in range(n + 1):
        T[0][j] = j

    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # else if current character of X and Y don't match
            else:
                T[i][j] = min(T[i - 1][j] + 1, T[i][j - 1] + 1)


# if __name__ == '__main__':
#     X = "ABCBDAB"
#     Y = "BDCABA"
#
#     m = len(X)
#     n = len(Y)
#
#     # lookup table stores solution to already computed sub-problems
#     # T[i][j] stores the length of SCS of substring X[0..i-1], Y[0..j-1]
#     T = [[0 for x in range(n + 1)] for y in range(m + 1)]
#
#     # fill lookup table in bottom-up manner
#     SCSLength(X, Y, m, n, T)
#
#     # find Shortest Common SuperSequence by reading lookup
#     # table in top-down manner
#     print("The Shortest Common SuperSequence of", X, "and", Y, "is", SCS(X, Y, m, n, T))