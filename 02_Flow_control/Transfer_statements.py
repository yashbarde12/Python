# Transfer Statements
'''
1. break : 
    Terminate the loop based on condition.

2. continue : 
    Skip current iteration and go for next based on condition.

3. pass : 
    Use this pass keyword when you don't want to write any code for a block/suit/body.
'''
#--------------------------------------------------------
prices = [199,299,99,199,399]
print("----  break  ------") 
for price in prices:
   if(price == 99):
      print("Terminating the loop because I got 99")
      break
      print("Statement after break") # This line will not execute because after statement.
   else:
      print(price, "added to cart")

#-------------------------------------------------------- 
print("----  continue  ------") 
      
for price in prices:
   if(price==99):
      # print("skipping the current iteration because I got 99")
      continue
      print("Statement after continue") #this line will not execute.
   else:
      print(price, "added to cart")

#--------------------------------------------------------
print("----  pass  ------")      
if (10 > 5):
   pass 

print("Statement after pass.")
   
#--------------------------------------------------------
#--------------------------------------------------------
   
