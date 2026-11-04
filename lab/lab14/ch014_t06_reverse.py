def reverse(text):
    result = ""
    # Iterate backwards through the string indices
    for i in range(len(text) - 1, -1, -1):
        result += text[i]
    return result
