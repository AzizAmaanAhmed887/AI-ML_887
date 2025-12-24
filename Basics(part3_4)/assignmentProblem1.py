string = input("Enter a palindrome string : ")


# logic to check if string is palindrome or not

def isPalindrome(string):
    string = string.lower()
    string.replace(" ", "")
    return string == string[::-1]


if isPalindrome(string):
    print(f"{string} is Palindrome")
else:
    print(f"{string}Not Palindrome")
