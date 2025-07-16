date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
if len(date) != 8 and date.isalpha():
    print("Invalid date format")
else:
    while len(date) > 1:
        Sum = 0
        for d in date:
            Sum += int(d)
        date = str(Sum)
    print("Your Digit of Life is: " + date)


'''
Output:
Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): 25052001
Your Digit of Life is: 6
'''
