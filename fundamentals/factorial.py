'''Write a program to calculate the factorial of a number.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
num = int(input("Enter any number : "))
fact = 1
a = 1
while a <= num:
    fact*=a
    a+=1
print(f"The factorial of {num} is {fact}.")
print()