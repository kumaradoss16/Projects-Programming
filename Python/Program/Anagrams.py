str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")
lst_1 = list(str_1.replace(" ", "").upper())
lst_2 = list(str_2.replace(" ", "").upper())

def sort_list(lst):
    length = len(lst)
    for i in range(length-1):
        first = i
        for j in range(i+1, length):
            if lst[j] < lst[first]:
                first = j
        lst[i], lst[first] = lst[first], lst[i]
    return "".join(lst)
    
if sort_list(lst_1) == sort_list(lst_2):
    print("Anagrams")
else:
    print("Not anagrams")

'''
Output:
Enter the first string: Listen
Enter the second string: Silent
Anagrams
'''
