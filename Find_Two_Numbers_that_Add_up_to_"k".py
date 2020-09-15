# In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and
# return two numbers that add up to k.
#
# Input #
# A list and a number k
#
# Output #
# A list with two integers a and b that add up to k
#
# Sample Input #
# lst = [1,21,3,14,5,60,7,6]
# k = 81
# Sample Output #
# lst = [21,60]

def find_sum(lst, k):
    # for i in range(len(lst)):
    #     for j in range(i+1, len(lst)):
    #         if (lst[i] + lst[j]) == k:
    #             return [lst[i], lst[j]]
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    sum = 0
    result = []
    while index1 != index2:
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append((lst[index2]))
            return result
    return False