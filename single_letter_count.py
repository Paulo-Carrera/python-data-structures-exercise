def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    count = 0
    for char in word:
        if char == letter.upper() or char == letter.lower():
            count += 1
    print(f"{letter.upper()}:{count}")


single_letter_count('apple pie', 'p')





