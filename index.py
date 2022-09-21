import datetime
import json
import platform
import subprocess
import sys
import time
import os

from colorama import Back, Fore, Style

config_text = """
{
    "config":{
        "prompt-start-text": "You can change the settings in the config file.",
        "prompt-title": "Python Command Prompt",
        "color_code": "COLOR_CODE.png",
        "prompt-color": "37",
        "prompt-time": "False",
        "bare": "|"
    }
}"""

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

def init():
    if os.path.exists('C:\\Users\\Public\\cmd'):
        if not os.path.exists('C:\\Users\\Public\\cmd\\config.json'):
            with open('C:\\Users\\Public\\cmd\\config.json', 'w') as file:
                file.write(config_text)
    else:
        os.makedirs('C:\\Users\\Public\\cmd\\command')
        init()

# def bare(type):
    # print(Style.BRIGHT + type + "| " + Style.RESET_ALL, end='')

init()
os.system('cls')
with open('C:\\Users\\Public\\cmd\\config.json', 'r') as file:
    configuration = json.load(file)
    config = configuration['config']
    file.close()
with open("C:\\Users\\Public\\cmd\\command.json", "r") as file:
    commandList = json.load(file)
    file.close()
now = datetime.datetime.now()
now2 = (now.strftime("%H:%M:%S %d/%m/%Y"))
loop = True
curpath = os.getcwd()
name_os = platform.system()
color = f"\x1b[{config['prompt-color']}m"
bare = config["bare"] + " "
    
os.system("title " + config['prompt-title'])



print(color + f"{name_os} Prompt\nVersion [1.0]\nCreator [Mathiol]\n{config['prompt-start-text']}\n")

while loop:
    try:
        # print(Style.BRIGHT + Fore.LIGHTBLACK_EX + "| " + Style.RESET_ALL, end='')
        now = datetime.datetime.now()
        now2 = (now.strftime("%H:%M:%S %d/%m/%Y"))
        curpath = os.getcwd()
        try:
            if config['prompt-time'] == "True":
                prompt_text = color + f"{now2} | {curpath}> "
            else:
                prompt_text = Style.BRIGHT + Fore.GREEN + bare + Style.RESET_ALL + color + f"{curpath}> "
            cmd = input(prompt_text)
        except EOFError: cmd = ""
        
        if cmd != "":
            # bare(Fore.LIGHTBLACK_EX)
            arg = ARGS(cmd)
            cmd = cmd.split()[0]
            cmd2 = f"command.{cmd}"
            exe = sys.executable
            if exe == "" or None:
                print("err")
            
            if cmd2 in commandList:
                path = "C:\\Users\\Public\\cmd\\command\\" + commandList[cmd2]['file']
                script = [sys.executable, path] + arg
                arg2 = ""
                for i in arg[0:]:
                    arg2 += i + ' '
                exe = os.system(f'python {path} {arg2}') #subprocess.call(script)
                # print(subprocess.CompletedProcess().stdout)
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