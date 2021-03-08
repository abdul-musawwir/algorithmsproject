
# from LCS import *

import time

# function call syntax
#exec_time(lambda: LCSLength(X, Y))


def exec_time(algo):
    # print(*args)
    start = time.time()
    data = algo()
    time.sleep(1)

    end = time.time()

    return data, end-start


# if __name__ == '__main__':
#     X = "XMJYAUZ"
#     Y = "MZJAWXU"
#     lcs_length = exec_time(lambda: LCSLength(X, Y))
#     print("The length of LCS is", lcs_length)
#     print(lcs_length[1])
