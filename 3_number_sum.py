def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    res = []
    for i in range(len(array)-2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            sum = array[i] + array[left] + array[right]
            if sum == targetSum:
                res.append([array[i], array[left], array[right]])
                left = left + 1
                right = right - 1
            elif sum < targetSum:
                left = left + 1
            else:
                right = right - 1
    return res

# time complexity: nlogn + n**2
# space: O(1)