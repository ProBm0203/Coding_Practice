'''Write a program to draw the pattern as shown below : 
0
2 2
4 4 4
8 8 8 8'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
print()
print(0)
two=1
for i in range (2,5):
    for j in range (0,i):
        print(2*two,end=" ")
    print()
    two*=2
print()