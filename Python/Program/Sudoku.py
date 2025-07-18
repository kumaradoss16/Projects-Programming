def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]
            
# A list of rows representing the sudoku.
rows = []
for r in range(9):
    ok = False
    while not ok:
        print(ok)
        row = input("Enter row #" + str(r+1) + ": ")
        ok = len(row) == 9 and row.isdigit()
        print(ok)
        if not ok:
            print("Incorrect row data - 9 digits required")
    rows.append(row)
ok = True

# Check if all rows are good
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break
    
# Check if all columns are good
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break
        
# Check if all sub-squares 3x3 are good
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ""
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break
            
if ok:
    print("Yes")
else:
    print("No")
