'''Write a program to read three numbers in three variables and swap first two variables with the sums of first and second, second and third numberes respectively.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
first=int(input("Enter the first number : "))
second=int(input("Enter the second number : "))
third=int(input("Enter the third number : "))
first=first+second
second=second+third
print(first,second,third)
print()