'''Write a program to demonstrate the pattern shown below : 
A
A B
A B C
A B C D
A B C D E
A B C D E F'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
lastChr=input("Enter the last alphabet you want : ")
if ord(lastChr)<=90:
    for i in range (65,ord(lastChr)+2):
        for j in range(65,i):
            print(chr(j),end=" ")
        print()
else: #for small alphabets
    for i in range (97,ord(lastChr)+2):
        for j in range(97,i):
            print(chr(j),end=" ")
        print()
print()
