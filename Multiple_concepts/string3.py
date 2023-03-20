"""Write a program to swap the first n characters of two strings. """

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
string1=input("Enter string1: ")  
string2=input("Enter string2: ")   
str1=""
str2=""
n=int(input("Enter the number of characters you want to swap: "))
if len(string1)>=n and len(string2)>=n:
    string1=list(string1)
    string2=list(string2)
    for i in range(0,n):
        string1[i],string2[i]=string2[i],string1[i]
    string1=str1.join(string1)
    string2=str2.join(string2)
    print("\nThe swapped strings are:")
    print(string1)
    print(string2)
    print()