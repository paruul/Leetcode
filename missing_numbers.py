def missingNumbers(nums):
    n = len(nums) + 2
    all_numbers = set(range(1, n + 1))
    given_numbers = set(nums)
    missing_numbers = list(all_numbers - given_numbers)
    return sorted(missing_numbers)