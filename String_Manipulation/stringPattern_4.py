'''Write a program to draw the pattern as shown below: 
    *   
  *   *
*   *   *
   ...
'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
lines=int(input("Enter how many lines you want to enter : "))
print()
leftSpace=lines-1
for i in range (1,lines+1):
    print(" "*leftSpace,end="")
    leftSpace-=1
    for j in range(0,i):
        print("*",end=" ")
    print()
print()

