from typing import List

s = input("Test if your word is a palindrome: ")


left,right = 0, len(s) -1
is_palindrome = True

while left < right:
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1

    if s[left].lower() != s[right].lower():
        print(s, "is NOT a palindrome!")
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print(s,"is a Palindrome")

