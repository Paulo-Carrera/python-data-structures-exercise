def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    count_num1 = {str(i): str(num1).count(str(i)) for i in range(10)}
    count_num2 = {str(i): str(num2).count(str(i)) for i in range(10)}
    return count_num1 == count_num2



print(same_frequency(123,321))
print(same_frequency(551122, 221515))
print(same_frequency(55112, 221515))
