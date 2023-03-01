def length_of_last_word(s):
    words = s.split()
    if not words:
        return 0
    return len(words[-1])
s = input("Enter a string: ")
length = length_of_last_word(s)
print("Length of the last word:", length)
