import sys

from colorama import Fore

chaine = ""
args = sys.argv
for e in args[1:]:
    chaine += ' ' + e
try:
    print(chaine)
except IndexError:
    print(Fore.RED + "Pas d'argument")
except Exception as e:
    print(e)