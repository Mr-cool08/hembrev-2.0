import tkinter as tk
from tkinter import ttk
from urllib.request import urlretrieve
import os
import configparser

def download_program(url):
    """Download program from URL."""
    # Replace the following line with your own logic for downloading the program
    # For demonstration purposes, this script just downloads a sample file from the URL
    filename = os.path.basename(url)
    urlretrieve(url, filename)

def install_program():
    """Install program from website."""
    # Replace the following URL with the URL of the program you want to install
    program_url = "https://example.com/program.exe"
    
    # Get user input for email addresses, username, and password
    email1 = email1_entry.get()
    email2 = email2_entry.get()
    email3 = email3_entry.get()
    email4 = email4_entry.get()
    email5 = email5_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    # Create a progress bar
    progress_bar = ttk.Progressbar(window, mode='indeterminate')
    progress_bar.pack(pady=10)
    progress_bar.start()
    
    # Download the program
    download_program(program_url)
    
    # Write email addresses, username, and password to config.ini file
    config = configparser.ConfigParser()
    config['EMAILS'] = {
        'email1': email1,
        'email2': email2,
        'email3': email3,
        'email4': email4,
        'email5': email5,
    }
    config['LOGIN'] = {
        'username': username,
        
    }
    with open('config.ini', 'w') as config_file:
        config.write(config_file)
    
    # Stop the progress bar
    progress_bar.stop()
    progress_bar.pack_forget()
    
    # Replace the following line with your own logic for installing the downloaded program
    # For demonstration purposes, this script just prints a message
    print("Program downloaded and installed successfully!")

# Create a Tkinter window
window = tk.Tk()
window.title("Program Installer")

# Create labels and entries for email addresses, username, and password
email1_label = tk.Label(window, text="Email 1:")
email1_label.pack()
email1_entry = tk.Entry(window)
email1_entry.pack()

email2_label = tk.Label(window, text="Email 2:")
email2_label.pack()
email2_entry = tk.Entry(window)
email2_entry.pack()

email3_label = tk.Label(window, text="Email 3:")
email3_label.pack()
email3_entry = tk.Entry(window)
email3_entry.pack()

email4_label = tk.Label(window, text="Email 4:")
email4_label.pack()
email4_entry = tk.Entry(window)
email4_entry.pack()

email5_label = tk.Label(window, text="Email 5:")
email5_label.pack()
email5_entry = tk.Entry(window)
email5_entry.pack()

username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show='*')
password_entry.pack()

# Create an Install button
install_button = tk.Button(window, text="Install", command=install_program)
install_button.pack()

# Run the Tkinter event loop
window.mainloop()
