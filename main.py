"""
Multiplication Table
"""

def print_multiplication_table(x : int, y : int) -> int:
    if x > 0 and y > 0:
        i = 1
        while i <= y:
            print(f"{i} * {x} = {i * x}")
            i += 1
    else:
        print("Number and rows cannot be les than 1")

"""
Palindromes
"""


def reverse(text: str) -> str:
    text = text.lower  # to make all lowercase
    text = str(text)
    text = text.replace(" ", "")  # to omit all spaces
    a = -1
    reversed_text = ""
    while a >= -len(text):
        reversed_text += text[a]
        a -= 1
    return reversed_text


def is_palindrome(text: str) -> bool:
    text = text.lower  # to make all lowercase
    text = str(text)
    text.replace(" ", "")  # to omit all spaces
    x = True
    y = False
    if text == reverse(text):  # something does not work here but I could not figure it out
        return x
    else:
        return y


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")
    is_palindrome("tami")
