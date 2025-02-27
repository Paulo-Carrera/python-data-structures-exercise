def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for i in lst:
        if not isinstance(i,list):
            return False
    return True






print(list_check([[123],[1,2,3],[123,123,123]]))
print(list_check([[1], "nope"]))