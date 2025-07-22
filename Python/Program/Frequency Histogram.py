from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
filename = input("Enter the file name: ")
try:
    with open(filename, "rt") as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    counters[char.lower()] += 1
        file.close()
        for char in counters.keys():
            c = counters[char]
            if c > 0:
                print(char, "->", c)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
