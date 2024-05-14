def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    true = []
    false = []
    for i in lst :
        if fn(i) == True:
            true.append(i)
        else :
            false.append(i)
    return f"{true} , {false}"


def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el,str)


print(partition([1,True,'False',False], is_string))
print(partition([1,2,3,4,5,6,7,8,9,10,11,12,13,14], is_even))