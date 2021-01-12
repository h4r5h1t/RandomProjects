#Ganesha Problem
#Print a Swastit Patteren for odd number of n input n>=5
#eg..  
'''
n=5
* ***
* *
*****
  * *
*** * 
'''
n = int(input("Enter the odd number: "))

#First Part
print("*",end="")
for i in range ((n-3)//2): #n-(n+1)/2-1 --> Remaing 
	print(" ",end="")
for i in range ((n+1)//2): 
	print("*",end="")
print("")
#Second Part
for i in range ((n-3)//2):
	#Star
	print("*",end="")
	#Space
	for i in range ((n-3)//2):
		print(" ",end="")
	#Star
	print("*")

#Third Part
for i in range (n):
	print("*",end="")
print('')

#Forth Part
for i in range ((n-3)//2):
	#Space
	for i in range (((n-3)//2)+1):
		print(" ",end="")
	#Star
	print("*",end="")
	#Space
	for i in range ((n-3)//2):
		print(" ",end="")
	#Star
	print("*")

#Fifth Part
for i in range ((n+1)//2):
	print("*",end="")
for i in range ((n-3)//2):
	print(" ",end="")
print("*")
