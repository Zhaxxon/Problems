# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.
# Name it merge_lists(lst1, lst2).
#
# Input #
# Two sorted lists.
#
# Output #
# A merged and sorted list consisting of all elements of both input lists.
#
# Sample Input #
# list1 = [1,3,4,5]
# list2 = [2,6,7,8]
# Sample Output #
# arr = [1,2,3,4,5,6,7,8]

def merge_lists(lst1, lst2):
    # merged_list = lst1 + lst2
    # return sorted(merged_list)
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0
    result = []

    for i in range(len(lst1) + len(lst2)):
        result.append(i)

    while (index_arr1 < len(lst1)) and (index_arr2 < len(lst2)):
        if lst1[index_arr1] < lst2[index_arr2]:
            result[index_result] = lst1[index_arr1]
            index_result += 1
            index_arr1 += 1
        else:
            result[index_result] = lst2[index_arr2]
            index_result += 1
            index_arr2 += 1

    while index_arr1 < len(lst1):
        result[index_result] = lst1[index_arr1]
        index_result += 1
        index_arr1 += 1

    while index_arr2 < len(lst2):
        result[index_result] = lst2[index_arr2]
        index_result += 1
        index_arr2 += 1

    return result