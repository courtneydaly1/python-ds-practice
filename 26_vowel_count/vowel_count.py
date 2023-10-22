def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    def vowel_count(phrase):
    # Initialize a dictionary to store vowel frequencies
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Convert the input phrase to lowercase for case-insensitivity
        phrase = phrase.lower()

    # Iterate through the characters in the phrase
        for char in phrase:
            if char in vowels:
                vowels[char] += 1

    # Remove keys with a frequency of 0 from the dictionary
        vowels = {key: value for key, value in vowels.items() if value > 0}

        return vowels



