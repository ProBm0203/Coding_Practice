#Author: Bhaskar Mishra
'''Write a program that reads the n to display nth term of Fibonacci series.
The Fibonacci sequence works as follows : 
- Element 0 has the value 0
- Element 1 has the value 1
- Every element after that has the value of the sumof the two preceding elements
The beginning of the sequence looks like : 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ....
For example: input7, produces 13'''


def fibonacci(n):
    L=[0,1]
    for i in range(n-1):
            L.append(L[-2]+L[-1])
    return(L[n])
    

# main (driver code)
print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
index=int(input("Enter which index you want : "))
number=fibonacci(index)
print(f"Number at index {index} is {number}")
print()