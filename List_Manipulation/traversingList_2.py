'''Write a program as per following specifications:
L is a list of numbers. Return a new list where each element is the corresponding element of list L summed with number num.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
L=eval(input("Enter the list : "))
num=int(input("Enter the number you want to add in the list: "))
newList=[]
for numbers in range (0,len(L)):
    newList.append(L[numbers]+num)
print(f"The new list is {newList}")
print()
