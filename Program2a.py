n = int(input("enter num of lines-"))
num = 1

for row in range(0, n):
    num = 1

    for j in range(0, row+1):
        print(num, end=" ")
        num = num + 1
    print("\r")
