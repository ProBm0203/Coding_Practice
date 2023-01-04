'''Write a program that reads from user - (i) an hour between 1 to 12 and (ii) number of hours ahead. The program should then print the time after those many hours, 
For Example:
Enter hour between 1-12 : 9
How many hours ahead : 4
Time at that time would be : 1 0'clock'''

print("---------------------------------\n     Author : Bhaskar Mishra     \n---------------------------------")
hour=int(input("Enter hour between 1-12 : "))
hoursAhead=int(input("How many hours ahead : "))
print("Time at that time would be : ",(hour+hoursAhead)%12,"0'clock")
print()