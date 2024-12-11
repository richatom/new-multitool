from modules.plugins.assets import *



def main():
    clear()
    setTitle()
    homeTitle()
    print(f'''
                                                                    {a}[{t}01{a}]{m} Windows Activator            {a}[{t}11{a}]{m} Linux Privacy Tool
                                                                    {a}[{t}02{a}]{m} Windows Optimizer
                                                                    {a}[{t}03{a}]{m} Winrar Activator
                                                                    {a}[{t}04{a}]{m} Mega Account Gen
                                                                    {a}[{t}05{a}]{m} Outlook Account Gen
                                                                    {a}[{t}06{a}]{m} Mediafire Bulk Downloader
                                                                    {a}[{t}07{a}]{m} Window Apps Downloader
                                                                    {a}[{t}08{a}]{m} Wfifi Password Cracker
                                                                    {a}[{t}09{a}]{m} Windows Privacy Tool
                                                                    {a}[{t}10{a}]{m} MacOS Privacy Tool
''')
    global choice
    choice = input(f'                                                         {a}Atom {t}==>>{m} ')
    
    if choice == '1':
        clear()
        exec(open('modules/atlasos/atlas.py').read())
    elif choice == '2':
        clear()
                

if __name__ == "__main__":
    clear()
    setTitle()
    main()