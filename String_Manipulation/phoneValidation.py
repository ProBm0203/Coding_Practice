'''Write a program that prompts for a phone number of 10 digits and two dashes, with dashes after the area code and the next three numbers. 
For example, 017-555-1212. Display if number entered is valid or invalid.'''


print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
phoneNumber=input("Enter your phone number : ")
number=""
if phoneNumber[3]=='-' and phoneNumber[7]=='-':
    for numbers in phoneNumber.split("-"):
        if numbers.isdigit():
            number+=numbers
    if len(number)==10:
        print("It's a valid phone number.")
    else:
        print("Invalid phone number.")    
else:
    print("Invalid phone number.")
print()