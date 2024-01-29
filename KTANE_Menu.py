# Main Program

# import functions with the format "from <fileName> import *"
# (* is similar to MySQL: read as, "from this file, import ALL functions")
from simpleWiresDialog import *

# fill in modules as you write them!
def printAvailableModules():
    print("***AVAILABLE MODULES***")
    print("Simple Wires")



print("********************************************************************************")
print("KTANE Helper")
print()
printAvailableModules()
print()

# ask for the module
module = input('Pick a module from the list above, or enter "DONE": ')

while module.upper() != "DONE":
    if module.upper() == "SIMPLE WIRES":
        simpleWiresDialog()
    else:
        print("I don't know anything about",module.upper())
    print()
    print()
    printAvailableModules()
    print()
    module = input('Pick a module, or enter "DONE": ')
    print()
