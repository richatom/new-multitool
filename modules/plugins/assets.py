import os
import platform
from colorama import Fore
import time
try:
    import termcolor
    import pyfiglet
    
except ModuleNotFoundError:
    os.system('pip install termcolor')
    os.system('pip install pyfiglet')

a = Fore.LIGHTMAGENTA_EX
t = Fore.LIGHTCYAN_EX
o = Fore.LIGHTRED_EX
m = Fore.LIGHTWHITE_EX
title = Fore.YELLOW


def clear():
    if platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def setTitle():
    if platform == 'Windows':
        os.system('-title Multitool - by Atom')
    else:
        print(' ')

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
\n""")