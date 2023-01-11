'''Write a program as per specifications below:
[1] Repeatedly prompt for a sentence or for 'q' to quit. 
[2] Upon input of a sentence s, print the string produced orm s by converting each lower case letter to upper case and each upper case letter to lower case. 
[3] All other characters are left unchanged.'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
sentence=input("Please enter your sentence, or 'q' to quit : ")
while sentence!='q':
    changed=""
    for i in range (0,len(sentence)):
        if sentence[i].islower():
            changed+=sentence[i].upper()
        elif sentence[i].isupper():
            changed+=sentence[i].lower()
        else:
            changed+=sentence[i]
    print(changed)
    sentence=input("Please enter your sentence, or 'q' to quit : ")
print()