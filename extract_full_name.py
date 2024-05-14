def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    full_names = [] 
    for p in people:
        first = p['first']
        last = p['last']
        full = (f"{first} {last}")
        full_names.append(full)
    return full_names






print(extract_full_names([
    {'first':'Paulo','last':'Carrera'},
    {'first':'Damian','last':'Alcala'},
    {'first':'God','last':'Zilla'}
]))