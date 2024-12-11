import subprocess
from plugins.assets import *

print('''We are not responsible for damages on your machine!
      Press y and Enter to continue
      ''')
a = input('')
if a == 'y':
    clear()
    try:
        subprocess.run(['runas', '/user:Administrator', 'windowsprivacytool.bat'], check=True)
    except Exception as e:
        print(f"Error: {e}")