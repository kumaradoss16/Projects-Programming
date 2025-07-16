text = input("Enter your message to encrypt: ")
text = text.replace(" ", "")
if len(text) > 1 and text.upper() == text[::-1].upper():
    print("It's a palindrome")
else:
    print("It's not a palindrome")

'''
Output:
Enter your message to encrypt: Eleven animals I slam in a net
It's not a palindrome
'''
