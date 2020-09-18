import os

VERSION=os.environ['VERSION']

VERSION = float(VERSION)
print ("The New Version is ----->" ,(VERSION + 1))
#os.system('echo "$VERSION 1" | awk '{print ${1} + ${2}}'')
