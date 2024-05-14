def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    result = []
    for num in nums :
        if num % 4 == 0 :
            triple = num * 3
            result.append(triple)
    return result 



print(triple_and_filter([4,8,12,16,20]))
print(triple_and_filter([1,2,3,4]))