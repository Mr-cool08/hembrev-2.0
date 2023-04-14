from configparser import ConfigParser
from cryptography.fernet import Fernet
import os
from progress.bar import Bar
import time
from encrpyt import *
import requests
import os, winshell, win32com.client
from pyunpack import Archive
import wget
from tqdm import tqdm

import zipfile
import sys
import shutil
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
isExist = os.path.exists('config.ini')
user = os.getlogin()
if isExist == False:
    print("Om du inte har flera epostadresser att skicka till lämna blankt")
    Aemail = input("skriv 1/5 av mailadresserna som ska få hembrevet: ")
    Bemail = input("skriv 2/5 av mailadresserna som ska få hembrevet: ")
    Cemail = input("skriv 3/5 av mailadresserna som ska få hembrevet: ")
    Demail = input("skriv 4/5 av mailadresserna som ska få hembrevet: ")
    Eemail = input("skriv 5/5 av mailadresserna som ska få hembrevet: ")
    login = input("skriv din Email som du ska skicka från: ")


    config_object = ConfigParser()
    
#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
    config_object["Emails"] = {
        "email1": Aemail,
        "email2": Bemail,
        "email3": Cemail,
        "email4": Demail,
        "email5": Eemail
    }
    config_object["login"] = {
        "email": login,
    }




#Write the above sections to config.ini file
    with open('config.ini', 'w') as conf:
        config_object.write(conf)
password = input("skriv ditt lösenord för eposten (Detta är nödvändigt): ")        
isExist = os.path.exists('hembrev.zip')
if isExist == False:
    print("Laddar ner...")
    wget.download("http://hembrev-1.mrcoolcool.repl.co")
# URL of the image to be downloaded is defined as image_url
    
    print("Klar!")

#PAPPA ÄR BÄST!



# string the key in a file



bar = Bar('Processing', max=3)
for i in range(1):
    with zipfile.ZipFile("hembrev.zip") as zf:
        for member in tqdm(zf.infolist(), desc='Extracting '):
            try:
                zf.extract(member, f"C:/Users/{user}/AppData/Roaming/")
            except zipfile.error as e:
                pass
    bar.next()
    with open('password.txt', 'w') as f:
        f.write(password)
    bar.next()
    encrypt()
    bar.next()
    try:
        shutil.move("config.ini", fr"C:/Users/{user}/AppData/Roaming/hembrev")
    except:
        pass
    bar.next()
    
    try:
        shutil.move("password-encrypted.txt", fr"C:/Users/{user}/AppData/Roaming/hembrev")
    except:
        pass
    bar.next()
    desktop = winshell.desktop()
    bar.next()
    #desktop = r"path to where you wanna put your .lnk file"
    path = os.path.join(desktop, 'Hembrev.lnk')
    bar.next()
    target = rf"C:\Users\{user}\AppData\Roaming\hembrev\hembrev.exe"
    bar.next()
    icon = f"C:/Users/{user}/AppData/Roaming/hembrev/Double-J-Design-Ravenna-3d-Mail.ico"
    
    bar.next()
    shell = win32com.client.Dispatch("WScript.Shell")
    bar.next()
    shortcut = shell.CreateShortCut(path)
    bar.next()
    shortcut.IconLocation = icon
    bar.next()
    shortcut.Targetpath = target
    bar.next()
    shortcut.save()
        
    bar.next()

    directory = "hembrev"
    bar.next()
        
    # Parent Directory path 
    parent_dir = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs"
    bar.next()
        
    # Path 
    path = os.path.join(parent_dir, directory) 
    bar.next()
    try:
        os.mkdir(path) 
    except:
        pass
    bar.next()
    desktop = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/hembrev"
    bar.next()
        #desktop = r"path to where you wanna put your .lnk file" 
    path = os.path.join(desktop, 'Hembrev.lnk')
    bar.next()
    target = rf"C:\Users\{user}\AppData\Roaming\hembrev\hembrev.exe"
    bar.next()
    icon = rf"C:\Users\{user}\AppData\Roaming\hembrev\Double-J-Design-Ravenna-3d-Mail.ico"
        
    bar.next()
    shell = win32com.client.Dispatch("WScript.Shell")
    bar.next()
    shortcut = shell.CreateShortCut(path)
    bar.next()
    shortcut.Targetpath = target
    bar.next()
    shortcut.IconLocation = icon
    bar.next()
    shortcut.save()
    bar.next()
    
    bar.next()
    desktop = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/hembrev"
    bar.next()
    #desktop = r"path to where you wanna put your .lnk file" 
    path = os.path.join(desktop, 'uninstall.lnk')
    bar.next()
    target = rf"C:\Users\{user}\AppData\Roaming\hembrev\uninstall.exe"
    bar.next()
    icon = rf"C:\Users\{user}\AppData\Roaming\hembrev\Double-J-Design-Ravenna-3d-Mail.ico"
    bar.next()

    shell = win32com.client.Dispatch("WScript.Shell")
    bar.next()
    shortcut = shell.CreateShortCut(path)
    bar.next()
    shortcut.Targetpath = target
    bar.next()
    shortcut.IconLocation = icon
    bar.next()
    shortcut.save()

    os.remove("hembrev.zip")



    # Directory 





    # Directory 

        
    # Create the directory 
    # 'GeeksForGeeks' in 
    # '/home / User / Documents' 






    bar.finish()
print("klar!")
input("Tryck på enter för att stänga: ")



