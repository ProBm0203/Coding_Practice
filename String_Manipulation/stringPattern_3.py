'''Write a program to draw the pattern as shown below:
* * * *
* * *
* *
*'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
lines=int(input("Enter the number of rows you want to enter : "))
for i in range(lines):
    for j in range(lines,i,-1):
        print("*",end=" ")
    print()
print()