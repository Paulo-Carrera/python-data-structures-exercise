def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    
    occurrences = {}

    for num in nums:
        occurrences[num] = occurrences.get(num,0) + 1
    
    max_count = max(occurrences.values())

    for num, count in occurrences.items():
        if count == max_count:
            return num
            

print(mode([0,1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5]))
print(mode([0,1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5]))
print(mode([0,1,1,2,2,2,3,3,3,3,4,4,5]))