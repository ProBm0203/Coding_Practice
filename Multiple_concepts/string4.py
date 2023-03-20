"""Write a program to input two strings and return the second string indices if it is present in the first string, else return -1"""

def indicesCheck(string1,string2):
    flag=0
    indices=[]
    for i in range(len(string1)):
        if (string1[i:i+len(string2)]==string2):
            indices.append(i)
            flag=1
    
    if flag==1:
        return indices
    else:
        return -1

#main or driver code
print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
string1=input("Enter the first string: ")
string2=input("Enter the second string: ")
indices=indicesCheck(string1,string2)
print(indices)
print()