from operator import sub
import subprocess,os,glob
import platform
from tkinter import E
from discord.ext.commands.errors import MissingPermissions
platforms=platform.system()

class MissingFile(Exception):
    pass

class IncorrectIntArgument(Exception):
    pass

rawpath=__file__.replace(os.getcwd(),"").split("/")[1:-1]
between="/"
str=""
for a in rawpath:
    str=str+a+between
path2= str
str=""
for a in rawpath:
    b=a.split(" ")
    c=""
    for d in b:
        c=c+d
    b=c
    if not b==a:
        a=f"\"{a}\""
    str=str+a+between
path=str

subprocess.call("clear",shell=True)

files=os.listdir(path2)

for a in files:
    if not a.endswith(".cpp"):
        files.pop(files.index(a))

if len(files)==0:
    raise MissingFile("In diesem Ordner befindet sich keine C++ Datei.")

if len(files)>=2:
    str=""
    for a in files:
        str=f"{str}{files.index(a)+1}: {a}\n"
    str=str+"\n"+": "
    choice=input(str)
    try:
        files=files[int(choice)-1]
    except Exception as e:
        subprocess.call("clear",shell=True)
        raise IncorrectIntArgument("Bitte schreibe eine korrekte Angabe in das Feld.")
else:
    files=files[0]

subprocess.call("clear",shell=True)

while True:
    subprocess.call(f"g++ -o r {path}{files}",shell=True)

    if "win" in platforms.lower():
        subprocess.call("r.exe",shell=True)
    else:
        subprocess.call("./r",shell=True)

    x=input("Drücke Enter um weiter zu kommen. ")
    subprocess.call("clear",shell=True)
    if x !="":
        exit()
