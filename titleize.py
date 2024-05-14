def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_chars = list(phrase)
    for i in range(len(phrase_chars)):
        if i == 0 or phrase_chars[i - 1] == ' ':
            phrase_chars[i] = phrase_chars[i].upper()
        else :
            phrase_chars[i] = phrase_chars[i].lower()
    return ''.join(phrase_chars)
            
        
      




print(titleize('wELCOME tO the paRTY!'))