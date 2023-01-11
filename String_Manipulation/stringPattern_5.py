'''Write a program to draw the pattern as shown below :
*
* *
* * *
* *
*
'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
peak=int(input("Enter the row at which you want the peak : "))
print()
for i in range(1,peak+1):
    for j in range(0,i):
        print("*",end=" ")
    print()
for k in range(1,peak):
    for l in range(k,peak):
        print("*",end=" ")
    print()
print()