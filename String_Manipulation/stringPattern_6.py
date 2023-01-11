'''Write a program to draw the pattern as shown below :
  *
 * *
* * *
 * *
  *'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
lines=int(input("Enter on which line you want the peak : "))
print()
leftSpace=lines-1
for i in range (1,lines+1):
    print(" "*leftSpace,end="")
    leftSpace-=1
    for j in range(0,i):
        print("*",end=" ")
    print()
leftSpace=1
for k in range (1,lines):
  print(" "*leftSpace,end="")
  leftSpace+=1
  for l in range (k,lines):
    print("*",end=" ")
  print()
print()