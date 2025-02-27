def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAEIOU"
    s = list(s)
    i , j = 0 , len(s) - 1

    while i < j :
        if s[i] in vowels and s[j] in vowels:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        elif s[i] not in vowels :
            i += 1
        elif s[j] not in vowels :
            j -= 1
        
    return ''.join(s)








print(reverse_vowels('Hello World!'))
print(reverse_vowels('welcome to jurassic park'))