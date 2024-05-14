def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    for p in parens:
        if parens.count("(") == parens.count(")"):
            return True
    else :
        return False
    




print(valid_parentheses('()'))
print(valid_parentheses('(())'))
print(valid_parentheses('(()())'))