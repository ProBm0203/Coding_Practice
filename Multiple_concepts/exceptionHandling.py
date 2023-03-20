"""Write a program to accept a name from a user. Raise and handle appropriate exception(s) if the text entered by the user contains digits and/or special characters."""

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
while True:
    try:
        name=input("Enter you name: ")
        for i in range(0,len(name)):
            if (name[i].isdigit()) or (not name[i].isalnum()):
                raise ValueError("Name should contain only alphabets")
    except ValueError as ve:
        print(ValueError)
    else:
        print(f"Hello, {name}!!!")
        print()
        break