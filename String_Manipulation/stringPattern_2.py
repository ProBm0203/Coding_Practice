'''Write a program to draw the pattern as shown below:
*
* *
* * *
* * * *'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
lines=int(input("Enter the number of rows you want : "))
for i in range(1,lines+2):
    for j in range(1,i):
        print("*",end=" ")
    print()
print()