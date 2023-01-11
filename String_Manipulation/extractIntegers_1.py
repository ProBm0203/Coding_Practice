'''Write a program that prompt the user for the string. Extract all the digits from the string. 
e.g., abc123 out--> abc123 has the digits 123 which sum to 6. e.g., abcd out--> abcd has no digits.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
alNumStr=input("Enter the string : ")
nums=""
sum=0
for i in range(0,len(alNumStr)):
    if alNumStr[i].isdigit():
        nums+=alNumStr[i]
        sum+=int(alNumStr[i])
if nums:
    print(f"{alNumStr} has the digits {nums} which sums to {sum}.")
else:
    print(alNumStr,"has no digits.")
print()