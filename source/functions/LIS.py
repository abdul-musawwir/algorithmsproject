# Iterative function to find length of longest increasing sub-sequence
# of given list
def LIS(A):
    # list to store sub-problem solution. L[i] stores the length
    # of the longest increasing sub-sequence ends with A[i]
    L = [0] * len(A)

    # longest increasing sub-sequence ending with A[0] has length 1
    L[0] = 1

    # start from second element in the list
    for i in range(1, len(A)):
        # do for each element in sublist A[0..i-1]
        for j in range(i):
            # find longest increasing sub-sequence that ends with A[j]
            # where A[j] is less than the current element A[i]
            if A[j] < A[i] and L[j] > L[i]:
                L[i] = L[j]

        # include A[i] in LIS
        L[i] = L[i] + 1

    # return longest increasing sub-sequence (having maximum length)
    return max(L)

#
# if __name__ == '__main__':
#     A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
#     print("Length of LIS is", LIS(A))