def fibonacci(n):
    p = pp = 1 
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            p, pp = pp, n
            yield n 
            
fibs = list(fibonacci(10))
print(fibs)

'''
Output:
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''
