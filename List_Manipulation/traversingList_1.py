'''Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements re sums of the corresponding elements in L and M.
For Example, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13]'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
L=eval(input("Enter the list L : "))
M=eval(input("Enter the list M : "))
N=[]
max=L
smax=M
if len(M)>len(max):
    max=M
    smax=L
for j in range (len(smax),len(max)+1):
    smax.append(0)
for i in range (0,len(max)):
    N.append(L[i]+M[i])

print("The third list N (sum of corresponding elements of M and N) : ",N)
print()