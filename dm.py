import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from dm import menu
    menu()
elif bit == '32bit':
    from SSB import bnsbuy
    bnsbuy()
