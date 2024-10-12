def firstDuplicateValue(array):
    seen_elems = set()
    for i in array:
        if i in seen_elems:
            return i
        seen_elems.add(i)
    return -1
