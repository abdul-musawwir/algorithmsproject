# Return true if there exists a sublist of list A[0..n) with given sum
def subsetSum(A, n, sum):
    # T[i][j] stores true if subset with sum j can be attained with
    # using items up to first i items
    T = [[False for x in range(sum + 1)] for y in range(n + 1)]

    # if sum is zero
    for i in range(n + 1):
        T[i][0] = True

    # do for ith item
    for i in range(1, n + 1):

        # consider all sum from 1 to sum
        for j in range(1, sum + 1):

            # don't include ith element if j-A[i-1] is negative
            if A[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                # find subset with sum j by excluding or including the ith item
                T[i][j] = T[i - 1][j] or T[i - 1][j - A[i - 1]]

    # return maximum value
    return T[n][sum]


# Return true if given list A[0..n-1] can be divided into two
# sublists with equal sum
def partition(A):
    total = sum(A)

    # return true if sum is even and list can can be divided into
    # two sublists with equal sum
    return (total & 1) == 0 and subsetSum(A, len(A), total // 2)


# if __name__ == '__main__':
#
#     # Input: set of items
#     A = [7, 3, 1, 5, 4, 8]
#
#     if partition(A):
#         print("Yes")
#     else:
#         print("No")