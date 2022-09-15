# utilising NUMPY
'''
import numpy as np

X = np.array([[1,1], [1,3]])
y = np.array([-56,8])
A= np.linalg.solve(X,y)
print(A)
'''
#Implementing Elimination

print("---------------- ---------------- DO NOT ENTER VARIABLES---------------- ----------------")

try:
    son = int(input("enter son's age (4 years ago):   "))
except ValueError:
    son = 1
father = int(input("how mANY times is fathers age from son(4 years ago):  "))

add = int(input("enter their sum after 4 years:   "))
x = 0
i = 0

while i != 1:
    if (son*x + 8) + (father*x + 8) == add:
        i = 1
        print(x)
    x += 1