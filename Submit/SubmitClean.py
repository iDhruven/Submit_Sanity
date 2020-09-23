import os

print ("------------------------------The Cleaning Begins here--------------------------------------")

print ("Cleaning Project...")
os.system('make clean > /dev/null')

# Clean MobileAssets
print ("Cleaning Mobile Assets...")
#os.system('cd MobileAssets')
os.system('cd MobileAssets | ./PopulateAssets.sh clean > /dev/null')
os.system('cd ..')

# Clean Python Morphun
print ("Cleaning Python Morphun...")
os.system('make -C interface/python clean > /dev/null')

print ("------------------------------The Cleaning Ends here--------------------------------------")
