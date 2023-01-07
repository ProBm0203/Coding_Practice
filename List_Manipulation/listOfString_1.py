'''Write a program that asks the user to enter a list of strings. Create new list that consists of those strings with their first characters removed.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
listOfStrings=eval(input("Enter a list of strings : "))
newList=[]
for i in range (0,len(listOfStrings)):
    newList.append(listOfStrings[i][1::])
print("\nOriginal list of strings : ",listOfStrings)
print("The new list of strings (first characters removed) : ",newList)
print()