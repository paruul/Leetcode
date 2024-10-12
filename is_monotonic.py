def isMonotonic(array):
    # Write your code here.
    if len(array) <= 2:
        return True
    left = 0
    right = 1
    inc = 0
    dec = 0
    while (left < right) and (right <= len(array)-1):
        if array[left] > array[right]:
            dec += 1
        elif array[left] < array[right]:
            inc += 1
        if dec > 0 and inc > 0:
            return False
        left=left+1
        right=right+1

    return True