def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    result = 1              #   initialize result to 1
    has_even = False        

    for n in nums:
        if n % 2 == 0:      
            result *= n
            has_even = True
    
    if has_even:
        return result
    else:
        return 1 









print(multiply_even_numbers([1,2,3,4,5,6,7,8,9,10]))
print(multiply_even_numbers([2,4,2]))

         