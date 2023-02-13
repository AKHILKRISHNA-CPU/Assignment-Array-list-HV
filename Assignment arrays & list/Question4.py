def is_palindrome(string):
    return string == string[::-1]
string = input("Enter a string to check either palindrome or not: ")
if is_palindrome(string):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
