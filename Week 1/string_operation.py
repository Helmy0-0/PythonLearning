def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aiueoAIUEO"
    return sum([1 for c in s if c in vowels])

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]