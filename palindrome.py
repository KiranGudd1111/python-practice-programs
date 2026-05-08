text = input("Enter text: ")

reverse = text[::-1]

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
