import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')
os.system('git pull')
os.system('xdg-open https://facebook.com/groups/3017062245271082/')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from zsb import bnsbuy
    bnsbuy()
elif bit == '32bit':
    from SSB import bnsbuy
    bnsbuy()
