'''Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). WAP to perform following operations: 
a. Print half the values of the tuple in one line and the other half in the next line. 
b. Print another tuple whose values are even numbers in the given tuple. 
c. Concatenate a tuple t2=(11,13,15) with t1. 
d. Return maximum and minimum value from this tuple '''

def halfTuples(t):
    midpoint = len(t) // 2
    first_half = t[:midpoint]
    second_half = t[midpoint:]
    print(first_half)
    print(second_half)

def evenTuple(t):
    t1 = []
    for i in range (len(t)):
        if t[i]%2==0:
            t1.append(t[i])
    print(tuple(t1))

def appendTuple(t):
    t2=(11,13,15)
    t=t+t2
    print(t)

def maxMinTuple(t):
    max_val = max(t)
    min_val = min(t)
    print("Maximum value:", max_val)
    print("Minimum value:", min_val)


#main or driver code
print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
halfTuples(t1)
evenTuple(t1)
appendTuple(t1)
maxMinTuple(t1)
print()