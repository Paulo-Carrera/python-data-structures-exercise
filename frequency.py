def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    count = 0
    for i in lst:
        if i == search_term:
            count += 1
    print (f"The frequency of {search_term} in this list is {count}.")





randomnums=[0,9,8,7,5,5,5,1,1,1,1,1,1,2,2,2,2,2,3,3,4,5,6,2,2,2,23,4,56,7,7,7,7,7,8,9]
frequency(randomnums, 5)

orders=['steak', 'chicken & waffles', 'spaghetti', 'steak', 'chicken & waffles', 'steak']
frequency(orders, 'chicken & waffles')







