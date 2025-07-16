text = input("Enter your message to encrypt: ")

shift = 0
while True:
    try:
        n = int(input("Enter a shift value (an integer from 1 to 25) :"))
        if 1 <= n <= 25:
            shift = n
            break
        else:
            print("Invalid shift value. Please enter a number between 1 and 25.")
    except ValueError:
        print("Invalid input. Please enter a integer number.")

cipher = ""
for char in text:
    if char.isalpha():
        if char.isupper():
            start_ascii = ord("A")
            code = ((ord(char) - start_ascii + shift) % 26) + start_ascii
        else:
            start_ascii = ord("a")
            code = ((ord(char) - start_ascii + shift) % 26) + start_ascii
        cipher += chr(code)
        
    else:
        cipher += char
        
        
print("Encoded text: ", cipher)


'''
Output:
Enter your message to encrypt: The die is cast
Enter a shift value (an integer from 1 to 25) :25
Encoded text:  Sgd chd hr bzr
'''
