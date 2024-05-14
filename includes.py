def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if isinstance(collection, (list, str, tuple)):
        if start is not None:
            for i in range(start,len(collection)):
                if collection[i] == sought:
                    return True
            return False
        else:
            return sought in collection
    elif isinstance(collection,(set,dict)):
        return sought in collection
    else:
        return False


print(includes([1,2,3,4,5,6,7,8,9,10],4,start=5))
print(includes([1,2,3,4,5,6,7,8,9,10],4,start=1))
print(includes([1,2,3,4,5,6,7,8,9,10],10,start=4))
print(includes('hello','l'))