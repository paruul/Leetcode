class Solution(object):
    """
    https://leetcode.com/problems/two-sum/description/
    Space complexity: O(n) due to the storage of indices in the dictionary.
    Time complexity: O(n) because we only loop through the list once.
    Logic: This problem can be efficiently solved using a hash map (or dictionary). 
    As you loop through the list, calculate the complement of each number (i.e., 
    the difference between the target and the current number). Store each number 
    along with its index in the dictionary as you go. For each number, check if 
    its complement is already in the dictionary—if it is, return the indices as a list.    
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_index.keys():
                return [num_index[complement], i]
            num_index[num] = i
        return []
        
        