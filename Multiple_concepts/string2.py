"""WAP to perform the following operations on a string 
a. Find the frequency of a character in a string. 
b. Replace a character by another character in a string. 
c. Remove the first occurrence of a character from a string. 
d. Remove all occurrences of a character from a string. 
"""

def frequency(string):
    freq_dict=dict()
    for i in range(0,len(string)):
        if string[i] in freq_dict:
            freq_dict[string[i]]+=1
        else:
            freq_dict[string[i]]=1
    print(freq_dict)

def replace(string):
    ch=input("Enter the character you want to replace: ")
    ch1=input("Enter the character you want to replace with: ")
    if ch in string:
        string=list(string)
        str1=""
        for i in range(0,len(string)):
            if string[i]==ch:
                string[i]=ch1
        string=str1.join(string)
        print(string)
    else:
        print("The character is not in the string")

def removeFirstOccurence(string):
    ch=input("Enter the character you want to remove: ")
    str=""
    if ch in string:
        string=list(string)
        for i in range(0,len(string)):
            if string[i]==ch:
                string.remove(ch)
                break
        print("The new string is: ",str.join(string))
    else:
        print("The character is not in the string")

def removeAllOccurences(string):
    ch=input("Enter the character you want to remove: ")
    str=""
    if ch in string:
        string=list(string)
        while (ch in string):
            string.remove(ch)
        print("The new string is: ",str.join(string))
    else:
        print("The character is not in the string")

#main or driver code
print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
string=input("Enter a string: ")
frequency(string)
replace(string)
removeFirstOccurence(string)
removeAllOccurences(string)
print()
