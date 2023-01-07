'''Write a program that ask the user to enter a list containing numbers between 1 and 12. Then replace all of the entries in the list that are greater than 10 with 10.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
listOf12=[]
replacedList=[]
for i in range (0,12):
    num=int(input(f"Enter the {i+1} entry : "))
    listOf12.append(num)
    if num<10:
        replacedList.append(num)
    elif num>10:
        replacedList.append(10)
print(f"The original list of 12 numbers is : {listOf12}")
print(f"The replaced list is : {replacedList}")
print()
