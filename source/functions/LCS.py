# Function to find length of Longest Common Subsequence of substring
# X[0..m-1] and Y[0..n-1]
def LCSLength(X, Y):
    m = len(X)
    n = len(Y)

    # lookup table stores solution to already computed sub-problems
    # i.e. T[i][j] stores the length of LCS of substring
    # X[0..i-1] and Y[0..j-1]
    Table = [[0 for x in range(n + 1)] for y in range(m + 1)]

    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                Table[i][j] = Table[i - 1][j - 1] + 1
            # else if current character of X and Y don't match,
            else:
                Table[i][j] = max(Table[i - 1][j], Table[i][j - 1])

    # LCS will be last entry in the lookup table
    return Table[m][n]


# if __name__ == '__main__':
#     X = "XMJYAUZ"
#     Y = "MZJAWXU"
#
#     print("The length of LCS is", LCSLength(X, Y))