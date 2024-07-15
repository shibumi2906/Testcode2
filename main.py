# main.py

def modulus(a, b):
    if b == 0:
        raise ValueError("На ноль делить нельзя")
    return a % b

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
