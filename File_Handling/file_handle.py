def totalCWL():
    num_words=0
    characters=0
    num_lines=0
    word="Y"
    with open('story.txt','r') as f:
        for line in f:
            num_lines+=1
            words = line.split()
            num_words+=len(words)
            for letter in line:
                for i in letter:
                    if i!="\n":
                        characters+=1

    print("The total lines in the file are: ",num_lines)
    print("The total words in the file are: ",num_words)
    print("The total characters in the file are: ",characters)

def frequency_c():
    with open('story.txt','r') as f:
        freq_dict=dict()
        for lines in f:
            for letter in lines:
                if letter!="\n":
                    if letter in freq_dict:
                        freq_dict[letter]+=1
                    else:
                        freq_dict[letter]=1
        print("\nThe frequency of each character is:")
        print(freq_dict)

def reverseWords():
    print("\nThe words of the file in the reversed order are: ")
    with open('story.txt','r') as f:
        for line in f:
            words = line.split()
            for word in words:
                print(word[::-1], end=" ")

def copyEvenLines():
    fin=open('story.txt','r')
    fout=open('file2.txt','w')
    lines=fin.readlines()
    for i in range(0, len(lines)):
        if (i%2 ==0):
            fout.write(lines[i])
        else:
            pass
    
    fout.close()
    fout=open('file2.txt','r')
    content=fout.read()
    print(f"\nThe content of file2 containing even line is :\n{content}")


totalCWL()
frequency_c()
copyEvenLines()
reverseWords()