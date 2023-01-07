'''Write a program as per following specifications: 
Return the lenth of the longest string in the list of strings str_list.
Precondition: the list will contain at least one element.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
str_list=eval(input("Enter the list of strings : "))
longestString=str_list[0]
for i in range (1,len(str_list)):
    if len(str_list[i])>len(longestString):
        longestString=str_list[i]

print("The longest string in the list is : ",longestString)   
print()