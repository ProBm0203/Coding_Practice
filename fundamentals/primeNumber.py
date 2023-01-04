'''Write a program to take a number in input and check whether it's a prime number or a composite.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
num=int(input("Enter any number : "))
mid=num//2
for integer in range (2,mid+1):
    if num%integer==0:
        print(f"The number {num} is composite.",end=" ")
        print(f"It's factor is {integer}.")
        break
else:
    print(f"The number {num} is prime.")
print()