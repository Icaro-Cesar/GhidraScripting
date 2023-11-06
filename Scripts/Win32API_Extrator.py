#@author Ox0d4y
#@category API Extrator

print("\nWin32 API Extrator\n")

# Create the pe_stable object, to access the getSymbolTable on currentProgram
pe_stable = currentProgram.getSymbolTable()
# Create the pe_exstable object, to acess the getExternalSymbols. Here we will collect the Imported Functions
pe_exstable = pe_stable.getExternalSymbols()

# Create a for loop, to print each Imported Function from the Import Table
for apis in pe_exstable:
     api = str(apis)  # Convert the type of apis variable to string
     print("------------------------------------------")
     print("Win32 API Name: "+api) # Print the results
     print("------------------------------------------")
