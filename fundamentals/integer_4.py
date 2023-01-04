'''Write a program to take 3-digit number and then print the reversed number. 
For example, if the input given is 123, the program should print 321.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
num=int(input("Enter a 3-digit number : "))
print("Reversed number is : ",end="")
print((num%100)%10,(num%100)//10,num//100,sep="")
print("OR")  #There is an another logic shown written below
num2=str(num)
num2=num2[-1::-1]
print(int(num2))
print()