import tkinter as tk
from tkinter import ttk
from urllib.request import urlretrieve
import os
import configparser
from pyshortcuts import make_shortcut
from configparser import ConfigParser
from cryptography.fernet import Fernet
import os
from swinlnk.swinlnk import SWinLnk
import os, winshell
from win32com.client import Dispatch
import pyuac
import zipfile
import logging
import threading
from progress.bar import Bar
import time
import wget
from tqdm import tqdm
from tkinter import messagebox
import zipfile
import sys
import datetime
import shutil
import subprocess
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from tkinter import ttk
from docx import Document
import datetime
import socket
import smtplib
import logging
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from windtalker import SymmetricCipher
import os
import configparser
import random
import tkinter as tk
from configparser import ConfigParser
from cryptography.fernet import Fernet
import time
import requests
import zipfile
import sys
import shutil
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import os
import requests
import socket

import socket
def main():
    def upload_file():
        """
        Uploads the "error.log" file to a Flask app via a POST request.

        Returns:
            str: The response from the Flask app.
        """
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'Error {host_name} {dt}.log')
        # Make sure the file exists before attempting to upload
        if os.path.exists(file_path):
            url = 'https://hembrev-3.mrcoolcool.repl.co/upload'
            files = {'file': open(file_path, 'rb')} # Open the file in binary mode

            response = requests.post(url, files=files)

            if response.status_code == 200:
                return 'File uploaded successfully'
            else:
                return 'File upload failed'
        else:
            return 'File not found'
    host_name = socket.gethostname()
    #getting the week number
    dt = datetime.date.today()
    wk = dt.isocalendar()[1]
    logging.basicConfig(filename=f'Error {host_name} {dt} installer.log', level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    def open_program():
        # Construct the path to the program
        program_path = os.path.join(os.environ['APPDATA'], 'hembrev', 'hembrev.exe')

        # Open the program using subprocess
        subprocess.Popen([program_path])

        # Close the tkinter window
        window.destroy()
    
    def download_program(url):
        """Download program from URL."""
        # Replace the following line with your own logic for downloading the program
        # For demonstration purposes, this script just downloads a sample file from the URL
        filename = os.path.basename(url)
        urlretrieve(url, filename)

    def install_program():
        path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming')
        newPath = path.replace(os.sep, '/')
        fullpath = newPath + "/hembrev"
        if os.path.exists(fullpath):
            try:
                shutil.rmtree(fullpath) #Delete the folder
                print("Folder deleted successfully.")
            except OSError as e:
                print(f"Failed to delete folder: {e}")
                logging.error('An error occurred: %s', e)
        else:
            pass
        installing = tk.Label(window, text="Laddar ner och installerar")
        installing.pack(pady=2)
        """Install program from website."""
        # Replace the following URL with the URL of the program you want to install
        program_url = "https://hembrev-3.mrcoolcool.repl.co/download"

        # Get user input for email addresses, username, and password

        # Create a progress bar
        progress_bar = ttk.Progressbar(window, mode='indeterminate')
        progress_bar.pack(pady=10)
        progress_bar.start()

        # Download the program
        print("downloading")
        download_program(program_url)
        def rename():
            old_name = "download"
            new_name = "hembrev.zip"
            try:
                os.rename(old_name, new_name)
            except FileExistsError as e:
                print(f"Failed to delete folder: {e}")
                logging.error('An error occurred: %s', e)
                result = upload_file()
                print(result)
                os.remove(new_name)
                rename()
        rename()
        # Write email addresses, username, and password to config.ini file

        # Stop the progress bar
        time.sleep(5)
        directory_to_extract_to = os.getenv('APPDATA')
        try:
            with zipfile.ZipFile("hembrev.zip", 'r') as zip_ref:
                zip_ref.extractall(directory_to_extract_to)
        except PermissionError as e:
            messagebox.showerror("Error", f"Du måste stänga programmet! \n \n {e}")
            logging.error('An error occurred: %s', e)
            window.destroy()
            
        """""
        path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming')
        newPath = path.replace(os.sep, '/')
        dst = "C:/Users/liam.suorsa08/OneDrive - Hudikgymnasiet/Desktop/programerings filer/python/hembrev/"
        shutil.copyfile(f"{newPath}/hembrev/hembrev", dst)"""""
        swl = SWinLnk()
        
        user_profile = os.path.expanduser('~')
        dest = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'hembrev.lnk')
        newdest = dest.replace(os.sep, '/')
        swl.create_lnk(f"{newPath}/hembrev/hembrev.exe", newdest)
        user_profile = os.path.expanduser('~')
        # Check if OneDrive folder exists in user profile directory
        onedrive_path = os.path.join(user_profile, 'OneDrive')
        if os.path.exists(onedrive_path):
            # Use OneDrive path as destination if OneDrive folder exists
            destination_path = os.path.join(onedrive_path, 'Skrivbord', "hembrev.lnk")
        else:
            # Use regular desktop path as destination if OneDrive folder doesn't exist
            destination_path = os.path.join(user_profile, 'Skrivbord', "hembrev.lnk")

        # Replace backslashes with forward slashes for destination path
        newdestination_path = destination_path.replace(os.sep, '/')
        appdata_path = os.getenv('APPDATA')
        start_menu_path = os.path.join(appdata_path, 'Microsoft', 'Windows', 'Start Menu')
        appdata_path = os.path.join(os.getenv('LOCALAPPDATA'), 'temp folder delete this')
        appdata_path = appdata_path.replace(os.sep, '/')
        
    # create the folder if it doesn't exist
        if not os.path.exists(appdata_path):
            os.makedirs(appdata_path)
            # Create shortcut
        appdata_path = appdata_path + "/hembrev.lnk"
        swl.create_lnk(f"{newPath}/hembrev/hembrev.exe", newdestination_path)
        swl.create_lnk(f"{newPath}/hembrev/hembrev.exe", appdata_path)
        shutil.copy(appdata_path, start_menu_path)
        os.remove(appdata_path)
        try:
            os.remove("hembrev.zip")
        except FileNotFoundError as e:
            print(f"Failed to delete folder: {e}")
            logging.error('An error occurred: %s', e)
            result = upload_file()
            print(result)
            pass
            
        # Replace the following line with your own logic for installing the downloaded program
        # For demonstration purposes, this script just prints a message
        install_button.pack_forget()
        installing.pack_forget()
        progress_bar.stop()
        progress_bar.pack_forget()
        ok_button = tk.Button(window, text='Öppna programmet', command=open_program)
        ok_button.pack(pady=2)
    def unistall():
        path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming')
        newPath = path.replace(os.sep, '/')
        fullpath = newPath + "/hembrev"
        if os.path.exists(fullpath):
            try:
                shutil.rmtree(fullpath) #Delete the folder
                print("Folder deleted successfully.")
            except OSError as e:
                print(f"Failed to delete folder: {e}")
                logging.error('An error occurred: %s', e)
        user_profile = os.path.expanduser('~')
        # Check if OneDrive folder exists in user profile directory
        onedrive_path = os.path.join(user_profile, 'OneDrive')
        if os.path.exists(onedrive_path):
            # Use OneDrive path as destination if OneDrive folder exists
            destination_path = os.path.join(onedrive_path, 'Skrivbord', "hembrev.lnk")
        else:
            # Use regular desktop path as destination if OneDrive folder doesn't exist
            destination_path = os.path.join(user_profile, 'Skrivbord', "hembrev.lnk")
        newdestination_path = destination_path.replace(os.sep, '/')
        try:
            os.remove(newdestination_path)
        except FileNotFoundError as e:
            print(f"Failed to delete folder: {e}")
            logging.error('An error occurred: %s', e)
            result = upload_file()
            print(result)
            pass
            
        appdata_path = os.getenv('APPDATA')
        start_menu_path = os.path.join(appdata_path, 'Microsoft', 'Windows', 'Start Menu')
        start_menu_path = start_menu_path + "/hembrev.lnk"
        start_menu_path = start_menu_path.replace(os.sep, '/')
        try:
            os.remove(start_menu_path)
        except FileNotFoundError as e:
            print(f"Failed to delete folder: {e}")
            logging.error('An error occurred: %s', e)
            result = upload_file()
            print(result)
            pass
        print("Program uninstalled successfully.")
        


    # Create a Tkinter window
    window = tk.Tk()
    window.title("Program Installer")

    # Create labels and entries for email addresses, username, and password
    def unstallstart():
        t = threading.Thread(name='Installing process', target=unistall)
        t.start()
    def start():
        t = threading.Thread(name='Installing process', target=install_program)
        t.start()
    # Create an Install button
    install_button = tk.Button(window, text="Installera / uppdatera", command=start)
    install_button.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)
    uninstall_button = tk.Button(window, text="Avinstallera", command=unstallstart)
    uninstall_button.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)


        
        
    window.geometry("400x300")
    # Run the Tkinter event loop
    window.mainloop()
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main()