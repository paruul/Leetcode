def zeroSumSubarray(nums):
    """For an array to contain a zero-sum subarray, if we compute 
    the cumulative sum of the elements and encounter the same sum 
    value more than once, it indicates the presence of a zero-sum 
    subarray. This is because for the sum to repeat, there must be 
    a subarray in between that sums to zero, bringing the cumulative 
    sum back to its previous value. Essentially, a repeated sum means 
    that the elements in the subarray between the two occurrences of 
    the same sum add up to zero."""
    zero_sum = set([0])
    running_sum = 0
    for i in nums:
        running_sum +=i
        if running_sum in zero_sum:
            return True
        zero_sum.add(running_sum)
    return False
