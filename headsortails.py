
import random 

def assignvars():  
	global heads 
	global tails 
	global throws
	global maxthrows 
	heads = 0
	tails = 0
	throws = 0
	maxthrows = int(input("Amount of coin flips? "))
		
assignvars()

def throwcoin (): 
	
	var1 = random.randint(1,2)	
	if var1 == 1 :
		global heads 
		heads += 1 			
		global throws
		throws += 1
	else:
		global tails
		tails += 1
		throws += 1 
		
throwcoin()

while throws < maxthrows:
	throwcoin()

print ("Heads: ",heads)
print ("Tails: ", tails)



