def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    a_hobbies=set(a[2])
    b_hobbies=set(b[2])
    common_hobbies = a_hobbies & b_hobbies
    if common_hobbies:
        print(f"Both {a[0]} and {b[0]} enjoy {common_hobbies}.")
        return True
    else:
        print(f"{a[0]} and {b[0]} have nothing in common.")
        return False
    


        
    
    





paulo = ('Paulo', 19, ['coding','fitness','sports','hiking','videogames','eating','sleeping'])
loki = ('Loki', 4, ['barking','eating','running','sleeping'])

print(friend_date(paulo,loki))

randomguy = ('idk', 444, ['singing', 'dancing', 'crying'])
randomgirl = ('girl', 000, ['dancing', 'hiking', 'barking', 'sleeping'])

print(friend_date(randomguy,randomgirl))
print(friend_date(loki,randomgirl))
print(friend_date(paulo,randomguy))










