import datetime
from itertools import chain
import json
import platform
from shutil import ExecError
import subprocess
import sys
import time
import os

from colorama import Back, Fore

def ARGS(com):
    try:
        com = com.split()[1:]
    except:
        com = com.split()
    return com

def cd(arg):
    try:    
        os.chdir(f"{arg[0]}") 
    except IndexError:
        print(os.getcwd())
    except Exception as e:
        print(e)

# def init():
#     if os.path.exists('C:\\Users\\Public\\Command'):
#         if not os.path.exists('C:\Users\Public\Command\config.json'):
#             with open('C:\Users\Public\config.json', 'w') as file:
#                 file.write("""{
#                     "config":{
#                     "prompt-start-text": "Bienvenue,",
#                     "prompt-title": "Terminal",
#                     "color_code": "COLOR_CODE.png",
#                     "prompt-color": "37",
#                     "prompt-time": "True"
#                 }
#             }""")
#     else:
#         os.mkdir('C:\Users\PublicCommand')
#         init()
# init()
os.system('cls')
with open('D:\Projet\Projets Python\Invite de commande +\config.json', 'r') as file:
    configuration = json.load(file)
    config = configuration['config']
    file.close()
with open("D:\Projet\Projets Python\Invite de commande +\command.json", "r") as file:
    commandList = json.load(file)
    file.close()
now = datetime.datetime.now()
now2 = (now.strftime("%H:%M:%S %d/%m/%Y"))
loop = True
curpath = os.getcwd()
name_os = platform.system()
color = f"\x1b[{config['prompt-color']}m"
    
os.system("title " + config['prompt-title'])



print(color + f"{name_os} Prompt\nVersion [1.0]\nCreator [Mathiol]\n{config['prompt-start-text']}\n")

while loop:
    try:
        now = datetime.datetime.now()
        now2 = (now.strftime("%H:%M:%S %d/%m/%Y"))
        curpath = os.getcwd()
        try:
            if config['prompt-time'] == "True":
                prompt_text = color + f"{now2} | {curpath}> "
            else:
                prompt_text = color + f"{curpath}> "
            cmd = input(prompt_text)
        except EOFError: cmd = ""
        
        if cmd != "":
            arg = ARGS(cmd)
            cmd = cmd.split()[0]
            cmd2 = f"command.{cmd}"
            
            if cmd2 in commandList:
                path = commandList[cmd2]['file']
                script = [sys.executable, path] + arg
                exe = subprocess.call(script)
                # if exe.returncode != 0:
                #     print(Fore.RED + f"Failed to execute «{cmd}»")
            elif cmd == "cd": cd(arg)
            else:
                try:
                    chaine = ""
                    for e in arg[0:]:
                        chaine += " " + e
                    os.system(cmd + chaine)
                except Exception as e:
                    print(Fore.RED + f"{cmd} : Le terme «{cmd}» n'est pas reconnu comme nom d'applet de commande, fonction, fichier de script ou programme exécutable. Vérifiez l'orthographe du nom, ou si un chemin d'accès existe, vérifiez que le chemin d'accès est correct et réessayez.\n\n{e}")
                    for l in str(e):
                        print('▹', end='')
                    print(f" Fin de la commande.\n")
    except KeyboardInterrupt: pass