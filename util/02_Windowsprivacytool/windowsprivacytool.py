import os
import ctypes
import sys

file = r'C:\Users\atom\Documents\GitHub\new-multitool\util\02_Windowsprivacytool\win.bat'
file2 = r'C:\Users\atom\Documents\GitHub\new-multitool\util\02_Windowsprivacytool\win2.bat'

def clear():
    if sys.platform.startswith('win32'):
        os.system('cls')
    elif sys.platform.startswith('cygwin'):
        os.system('cls')

def question():
    choice = input('System or app? (s/a):\n ')
    if choice == 's':
        clear()
        privacytool(file)
    elif choice == 'a':
        clear()
        apptool(file2)

def privacytool(path):

    script = f'cmd /c "{path}"'
    params = f'/c {script}'
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", params, None, 1)
    except Exception as e:
        print(f"Failed to elevate privileges: {e}")

def apptool(path):
    script = f'cmd /c "{path}"'
    params = f'/c {script}'
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", params, None, 1)
    except Exception as e:
        print(f"Failed to elevate privileges: {e}")


# privacytool(file)
if __name__ == "__main__":
    clear()
    question()