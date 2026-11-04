def anti_vowel(text):
    result = ""
    vowels = "aeiouAEIOU"
    for char in text:
        if char not in vowels:
            result += char
    return result