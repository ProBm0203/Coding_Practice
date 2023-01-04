'''Write a program to take two inputs for day, month and then calculate which day of the year, the given date is. For simplicity, take 30 days for all months. 
For example, if you give innput as: Day3, Month2 then it should print "Day of the year: 33".'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
day=1
month=30
d=int(input("Enter the day : "))
m=int(input("Enter the month : "))
print("Day of the year : ",(month*(m-1))+(day*d))
print()