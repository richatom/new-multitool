from modules.plugins.assets import *

def main():
    clear()
    setTitle()
    homeTitle()

    print(f'''\n{a}[{t}++{o}]{m} Main options:                            {a}[{t}++{o}]{m} Account options:               {a}[{t}++{o}]{m} Download options:
{a}[{t}01{o}]{m} Windows Activator                        {a}[{t}04{o}]{m} Mega Account Gen               {a}[{t}07{o}]{m} Mediafire Bulk Downloader
{a}[{t}02{o}]{m} Windows AtlasOS                          {a}[{t}05{o}]{m} Outlook Account Gen            {a}[{t}08{o}]{m} Windows Apps Downloader
{a}[{t}03{o}]{m} Winrar Activator                         {a}[{t}06{o}]{m} not yet a tool                 {a}[{t}09{o}]{m}
  ''')
    global choice
    choice = input()
if __name__ == "__main__":
    clear()
    setTitle()
    main()