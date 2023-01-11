'''Write a program that takes two strings from the user and displays the smaller string in single line and the larger string as per this format:
 1st letter                        last letter
   2nd letter              2nd last letter
       3rd letter      3rd last letter
                   ...  '''


print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
string1=input("Enter the first word : ")
string2=input("Enter the second word : ")
maxString=string1
shorterString=string2
if len(string2)>len(maxString):
    maxString=string2
    shorterString=string1
print(shorterString)
mid=len(maxString)//2
spaceBetween=mid
spaceLeft=0
for i in range (0,mid):
    print(i*'\t'+maxString[i]+(spaceBetween*'\t')*2+maxString[-(i+1)])
    spaceBetween-=1
    spaceLeft=i
if len(maxString)%2!=0:
    print((spaceLeft+1)*'\t'+maxString[mid])
print()