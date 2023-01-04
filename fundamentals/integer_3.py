'''Write a program to take 2-digit number and then print the reversed number. 
For example, if the input given is 25, the program should print 52.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
num=int(input("Enter a 2-digit number : "))
print("Reversed number is : ",end="")
print(num%10,num//10,sep="")
print()