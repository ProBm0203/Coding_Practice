'''Write a program that rotates the elements of a list so that the element at the first index moves to the second index, the element in the second index moves to the third index, etc., and the element in the last index moves to the first index.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
array=eval(input("Enter a List : "))
rotatedArray=[]
rotatedArray.append(array[-1])
for i in range (0,len(array)-1):
    if i!=len(array):
        rotatedArray.append(array[i])
print("The Rotated List : ",rotatedArray)
print()