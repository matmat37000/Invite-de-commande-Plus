import os
import sys

chaine = ""
args = sys.argv
for e in args[1:]:
    chaine += ' ' + e
    
try:    
    os.chdir(f"{args[1]}") 
    print(os.getcwd())
except IndexError:
    print(os.getcwd())
except Exception as e:
    print(e)