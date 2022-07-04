import json
import os
import webbrowser
import sys

from colorama import Fore
import cv2

answer_liste = ["  1) Open it", "  2) Don't open it"]
with open('D:\Projet\Projets Python\Invite de commande +\config.json', 'r') as file:
    configuration = json.load(file)
    config = configuration['config']
    file.close()
color = f"\x1b[{config['prompt-color']}m"
chaine = ""
args = sys.argv
for e in args[1:]:
    chaine += ' ' + e

def READ(NAME):
    d = cv2.QRCodeDetector()
    try: 
        val, points, qrcode = d.detectAndDecode(cv2.imread(f'{NAME}.png'))
    except:
        path = os.path.abspath(f"{NAME}.png")
        print(f"QRCODE '{path}' cannot be found and/or read, check the spelling and that the image file exists.")
    else:
        print(f"Valeur du QR Code: {Fore.LIGHTBLUE_EX + val + color}")
        
        if "http" in val:
            loop = True
            while loop:
                print("Your QRCODE contains a link, do you want to open it ?\n")
                for a in answer_liste:
                    print(a)
                    
                answer = input("\n  -> ")
                if answer == "1":
                    webbrowser.open(val)
                    loop = False
                    break
                elif answer == "2":
                    loop = False
                else:
                    print(f"Is not a number between 1-{len(answer_liste)}")

try:                   
    READ(NAME=args[1])
except IndexError: "Please pass as argument the name, like here: 'read NAME'"