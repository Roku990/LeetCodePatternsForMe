from typing import List

s = input("Test if your word is a palindrome: ")


left,right = 0, len(s) -1
is_palindrome = True

## while the word is not done
while left < right:
    # check for spaces and number in left and right
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1

    # ignore caps and check if theyre not the same
    if s[left].lower() != s[right].lower():
        # if not the same then break and print that its not a palindrome
        print(s, "is NOT a palindrome!")
        is_palindrome = False
        break
    ## add one to each slide so that they check the next letters
    left += 1
    right -= 1
## if it is a palindrome, print that it is and end the program! :D
if is_palindrome:
    print(s,"is a Palindrome")

