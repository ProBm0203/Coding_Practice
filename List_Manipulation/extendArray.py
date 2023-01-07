'''Write a program that inputs two lists and creates a third, that contains all elements of the first folowed by all elements of the second.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
firstList=eval(input("Enter the first list : "))
secondList=eval(input("Enter the second list : "))
thirdList=[]
#traditional method
for first in range (0,len(firstList)):
    thirdList.append(firstList[first])
for second in range (0, len(secondList)):
    thirdList.append(secondList[second])
print("The third list using traditional method : ",thirdList)

#Modern Method
thirdList.clear()
thirdList.extend(firstList)
thirdList.extend(secondList)
print("The third list using modern method : ",thirdList)
print()