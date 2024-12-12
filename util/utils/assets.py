import os
import platform
from colorama import Fore
import time
import sys

try:
    import termcolor
    import pyfiglet
    import keyboard
    import subprocess
    import certifi
    import charset_normalizer
    import gazpacho
    import idna
    import requests
    import urllib3
except ModuleNotFoundError:
    os.system('pip install termcolor')
    os.system('pip install pyfiglet')
    os.system('pip install keyboard')
    os.system('pip install subprocess')
    os.system('pip install certifi')
    os.system('pip install charset-normalizer')
    os.system('pip install gazpacho')
    os.system('pip install idna')
    os.system('pip install requests')
    os.system('pip install urllib3')

a = Fore.LIGHTMAGENTA_EX
t = Fore.LIGHTCYAN_EX
o = Fore.LIGHTRED_EX
m = Fore.LIGHTWHITE_EX
title = Fore.YELLOW


def clear():
    if sys.platform.startswith('win32'):
        os.system('cls')
    elif sys.platform.startswith('cygwin'):
        os.system('cls')
    elif sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('darwin'):
        os.system('clear')

def setTitle():
    if sys.platform.startswith('win32'):
        os.system('title Multitool -by Atom')
    elif sys.platform.startswith('cygwin'):
        os.system('title Multitool -by Atom')
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;Multitool -by Atom\x07")
    elif sys.platform.startswith('darwin'):
        sys.stdout.write("\x1b]2;Multitool -by Atom\x07")
def homeTitle():
    print(f"""
                                                                {m}+=================================================================================================+
                                                                |{title}                                                                                                 {m}|
                                                                |{title}                                                                                                 {m}|
                                                                |{title}      ▄████████  ▄█        ▄█             ▄█  ███▄▄▄▄         ▄██████▄  ███▄▄▄▄      ▄████████   {m}|
                                                                |{title}     ███    ███ ███       ███            ███  ███▀▀▀██▄      ███    ███ ███▀▀▀██▄   ███    ███   {m}|
                                                                |{title}     ███    ███ ███       ███            ███▌ ███   ███      ███    ███ ███   ███   ███    █▀    {m}|
                                                                |{title}     ███    ███ ███       ███            ███▌ ███   ███      ███    ███ ███   ███  ▄███▄▄▄       {m}|
                                                                |{title}   ▀███████████ ███       ███            ███▌ ███   ███      ███    ███ ███   ███ ▀▀███▀▀▀       {m}|
                                                                |{title}     ███    ███ ███       ███            ███  ███   ███      ███    ███ ███   ███   ███    █▄    {m}|
                                                                |{title}     ███    ███ ███▌    ▄ ███▌    ▄      ███  ███   ███      ███    ███ ███   ███   ███    ███   {m}|
                                                                |{title}     ███    █▀  █████▄▄██ █████▄▄██      █▀    ▀█   █▀        ▀██████▀   ▀█   █▀    ██████████   {m}|
                                                                |{title}                ▀         ▀                                                                      {m}|
                                                                |{title}                                   {title}[{a}github.com/richatom{title}]                                         {m}|
                                                                {m}+=================================================================================================+                                                                                                                                
                                                                """)