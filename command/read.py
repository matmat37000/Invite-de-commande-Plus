import os
import webbrowser
from colorama import Fore
import cv2

answer_liste = ["  1) Open it", "  2) Don't open it"]

def READ():
    NAME = input("QRCODE name: ")
    d = cv2.QRCodeDetector()
    try: 
        val, points, qrcode = d.detectAndDecode(cv2.imread(f'./QRCODE/{NAME}.png'))
    except:
        path = os.path.abspath(f"./QRCODE/{NAME}.png")
        print(f"QRCODE '{path}' cannot be found and/or read, check the spelling and that the image file exists.")
    else:
        print(f"Valeur du QR Code: {Fore.LIGHTBLUE_EX + val + Fore.WHITE}")
        
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
                    print("Exit.")
                    loop = False
                else:
                    print(f"Is not a number between 1-{len(answer_liste)}")
        else:
            input()