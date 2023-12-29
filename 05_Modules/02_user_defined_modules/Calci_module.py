
def add(x, y):
   return x + y

def sub(x, y):
   return x - y

#--------------------------------------------------------
# Taking Random variable name and accessing a value
name = "jim"
#--------------------------------------------------------
# Checking value of __name__
print("value of __name__:", __name__) # value of __name__: __main__
#--------------------------------------------------------
# Checking this program act as individual or as module to other program.
if (__name__ == "__main__"):
    print("This file is executed directly.")
else:
    print("This file executed by some other file as a module.")
#--------------------------------------------------------
#--------------------------------------------------------