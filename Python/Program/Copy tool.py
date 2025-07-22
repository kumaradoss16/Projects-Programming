from os import strerror

srcname= input("Enter the source file name: ")
dstname = input("Enter the destination file name: ")
try:
    with open(srcname, "rb") as src:
        with open(dstname, "wb") as dst:
            buffer = bytearray(65536)
            total = 0
            readin = src.readinto(buffer)
            while readin > 0:
                written = dst.write(buffer[:readin])
                total += written
                readin = src.readinto(buffer)
except IOError as e:
        print("Cannot open the source file: ", strerror(e.errno))
        exit(e.errno)
