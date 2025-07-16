digits = ["1111110", "0110000", "1101101", "1111001",
"0110011", "1011011", "1011111", "1110000", "1111111", 
"1110011"]

def print_number(num):
    global digits
    digs = str(num)
    lines = ['' for _ in range(5)]
    for d in digs:
        segs = [[" ", " ", " "] for _ in range(5)]
        ptrn = digits[ord(d) - ord("0")]
        if ptrn[0] == "1":
            segs[0][0] = segs[0][1] = segs[0][2] = "*"
        if ptrn[1] == "1":
            segs[0][2] = segs[1][2] = segs[2][2] = "*"
        if ptrn[2] == "1":
            segs[2][2] = segs[3][2] = segs[4][2] = "*"
        if ptrn[3] == "1":
            segs[4][0] = segs[4][1] = segs[4][2] = "*"
        if ptrn[4] == "1":
            segs[4][0] = segs[3][0] = segs[2][2] = "*"
        if ptrn[5] == "1":
            segs[0][0] = segs[1][0] = segs[2][0] = "*"
        if ptrn[6] == "1":
            segs[2][0] = segs[2][1] = segs[2][2] = "*"
        for lin in range(5):
            lines[lin] += ''.join(segs[lin]) + ' '
    for lin in lines:
        print(lin)
        
print_number(int(input("Enter the number you wich to diplay: ")))



"""
Enter the number you wich to diplay: 12345
  * *** *** * * *** 
  *   *   * * * *   
  * *** *** *** *** 
  * *     *   *   * 
  * *** ***   * ***
"""
