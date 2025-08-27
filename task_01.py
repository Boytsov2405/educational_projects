def is_palindrome(_line) -> bool:
    _converting = "".join(_ch.lower() for _ch in str(_line) if _ch.isalnum())
    return _converting==_converting[::-1]

print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))

print(is_palindrome(input("Enter text: ")))