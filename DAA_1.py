def find_word(text, pattern):
    text_lower = text.lower()
    pattern_lower = pattern.lower()
    n = len(text_lower)
    m = len(pattern_lower)
                             
    for i in range(n - m + 1):
        if text_lower[i:i+m] == pattern_lower:
            print(f'"{pattern}" word exists!')
            print(f'"{pattern}" word is in the index {i} and ending {i + m - 1}')
            return
    print(f'"{pattern}" word does not exist!')
text = "The Dog is barking."
pattern = "DOG"
find_word(text, pattern)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        