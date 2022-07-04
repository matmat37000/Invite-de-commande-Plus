import os
import sys
import time
from colorama import Fore

from qrcode import ERROR_CORRECT_H, ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q
import qrcode

chaine = ""
args = sys.argv
for e in args[1:]:
    chaine += ' ' + e

def qrcodegen(NAME, DATA, VERSION=1, ERROR=ERROR_CORRECT_L, BOX_SIZE=10, BORDER=4):
    qr = qrcode.QRCode(
    version=VERSION,
    error_correction=ERROR,
    box_size=BOX_SIZE,
    border=BORDER,
    )
    qr.add_data(DATA)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    try:
        img.save(f"{NAME}.png")
    except:
        print("The QRCODE '" + Fore.LIGHTBLUE_EX + f"{NAME}.png" + Fore.RESET + "' cannot be created !")
    else:
        path = os.path.abspath(f"{NAME}.png")
        print(f"Image save in '{Fore.LIGHTBLUE_EX + path + Fore.RESET}'")# \\{NAME}.png")

try:       
    qrcodegen(args[1], args[2])
except IndexError: print(Fore.RED + "Please pass as argument the name and then the data, like here: 'qrcode NAME DATA'")