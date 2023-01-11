'''Write a program that takes two inputs: first an integer and the second, a string.
From the input string extract all the digits, in the order they occurred, from the string. If no digits found set the extracted digits to 0.
Add the integer inputand the digits extracted from the string together as integers.'''


print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
integer=int(input("Enter an integer : "))
string=input("Enter a string : ")
extractedNumbers=''
for i in range(0,len(string)):
    if string[i].isdigit():
        extractedNumbers+=string[i]
if extractedNumbers:
    print(f"The integer given is {integer}")
    print(f"The sum of integer {integer} and extracted number {extractedNumbers} is : ",integer+int(extractedNumbers))
else:
    print(f"The integer given is {integer}")
    print(f"The sum of integer {integer} and extracted number 0 is : ",integer)
print()