in1 =  input("enter num, alphabet or special char-")
if (in1>='a' and in1<='z') or (in1>='A' and in1<='Z'):
    print("is an alphabet")
elif (in1>='1' and in1<='9'):
    print("is an number")
else:
    print("it is a special character")