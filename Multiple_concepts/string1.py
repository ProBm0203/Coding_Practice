'''Write a program that accepts a character and performs the following: 
a. print whether the character is a letter or numeric digit or a special character 
b. if the character is a letter, print whether the letter is uppercase or lowercase 
c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output is NINE) '''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
def characterRecog(ch):
    if ch>='0' and ch<='9':
        print("The character entered is a numeric digit.")
        ch=int(ch)
        lst=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
        for i in range (0,10):
            if ch==i:
                print(f"&\nThe character is {lst[i]}")
    elif (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        print("The character entered is a letter.")
        if ch.isupper():
            print("&\nThe character is in uppercase.")
        else:
            print("&\nThe character is in lowercase.")

    else:
        print("The input is a special character.")

#main or driver code
character=input("Enter a character: ")
characterRecog(character)
print()

