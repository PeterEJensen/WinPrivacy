import winreg
import ctypes, os


REG_PATH = r"Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\FileExts\\.pdf\\UserChoice"
REG_PATH1 = r"SYSTEM\CurrentControlSet\\Services\\DiagTrack"
REG_PATH2 = r"SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection"
REG_PATH3 = r"System\\GameConfigStore"
REG_PATH4 = r"SYSTEM\\CurrentControlSet\\Services\\dmwappushservice"
REG_PATH5 = r"SOFTWARE\\Microsoft\\Windows Defender\\Spynet"

print(r'''
__        __ ___  _   _  ____   ____   ___ __     __    _      ____ __   __
\ \      / /|_ _|| \ | ||  _ \ |  _ \ |_ _|\ \   / /   / \    / ___|\ \ / /
 \ \ /\ / /  | | |  \| || |_) || |_) | | |  \ \ / /   / _ \  | |     \ V /
  \ V  V /   | | | |\  ||  __/ |  _ <  | |   \ V /   / ___ \ | |___   | |
   \_/\_/   |___||_| \_||_|    |_| \_\|___|   \_/   /_/   \_\ \____|  |_|
    
            Stay private, stay incognito!                   [Peter Jensen]
''')


def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin


def set_tele(name = 'AllowTelemetry'):
    try:                    
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH2, 2,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)  
    except WindowsError:
        return None

    if value != 0:
        try:
            winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH2)
            
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH2, 2, 
                                        winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 2, winreg.REG_DWORD, 0)
            winreg.CloseKey(registry_key)
            print('successfully disabled telemetry!')
            return True
        except WindowsError:
            print('failed telemetry')
            print(WindowsError)
            return False
    else:
        print("Already disabled Telemetry. Nothing changed.")

def set_diagTrack(name = 'Start'):
    try:                    
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH1, 2,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
    except WindowsError:
        return None
    if value != 4:
        try:
        #print('disabling Diagtrack..')
            winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH1)
            
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH1, 2, 
                                        winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 2, winreg.REG_DWORD, 4)
            winreg.CloseKey(registry_key)
            print('successfully disabled DiagTrack!')
            return True
        except WindowsError:
            print('failed DiagTrack')
            print(WindowsError)
            return False
    else:
        print('Already disabled DiagTrack. Nothing changed.')


def set_gameDVR(name = 'GameDVR_Enabled'):
    try:                    
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH3, 2,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
    except WindowsError:
        return None

    if value !=0:
        try:
            winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH3)
            
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH3, 2, 
                                        winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 2, winreg.REG_DWORD, 0)
            winreg.CloseKey(registry_key)
            print('successfully disabled gameDVR!')
            return True
        except WindowsError:
            print('failed gameCVR')
            print(WindowsError)
            return False
    else:
        print('Already disabled GameDVR. Nothing changed.')





def set_dmwapp(name = 'Start'):
    try:                    
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH4, 2,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
    except WindowsError:
        return None
    if value !=4:
        try:
            winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH4)
            
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH4, 2, 
                                        winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 2, winreg.REG_DWORD, 4)
            winreg.CloseKey(registry_key)
            print('successfully disabled dmwappushservice!')
            return True
        except WindowsError:
            print('failed dmwappushservice')
            print(WindowsError)
            return False
    else:
        print('Already disabled dmwappushservice. Nothing changed.')
        



running = True
while running:
    print("""
    1.Clear all tracking from windows
    2.Exit
    """)

    running=input(" ")
    if running =='1':
        if isAdmin():
            print('Running as admin - Continuing..')
            print('********************************')
            set_tele() # OK
            set_diagTrack() # OK
            set_gameDVR() # OK
            set_dmwapp() # OK
            #set_SpyNet() # -
            #set_SampleConsent() # -
        else:
            print('Please rerun this program as admin')
    elif running =='2':
        running = None
    else:
        print('Not a valid choice.')



###################################
# outcommented for now, as windows protects defender regedit settings
###################################
"""
def set_SpyNet(name = 'SpyNetReporting'):
    try:                    
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH5, 2,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
    except WindowsError:
        return None
    print('Spynet value: ', value)
    if value !=0:
        try:
            winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH5)
            
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH5, 2, 
                                        winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 2, winreg.REG_DWORD, 0)
            winreg.CloseKey(registry_key)
            print('successfully disabled SpyNetReporting!')
            return True
        except WindowsError:
            print('failed SpyNetReporting')
            return False
    else:
        print('Already disabled SpyNetReporting. Nothing changed.')

def set_SampleConsent(name = 'SubmitSamplesConsent'):
    try:                    
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH5, 2,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
    except WindowsError:
        return None
    if value != 2:
        try:
            winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH5)
            
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\Microsoft\Windows Defender\\Spynet", 2, 
                                        winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 2, winreg.REG_DWORD, 2)
            winreg.CloseKey(registry_key)
            print('successfully disabled SamplesConsent!')
            return True
        except WindowsError:
            print('failed SamplesConsent')
            print(WindowsError)
            return False
    else:
        print('Already disabled SubmitSamplesConsent. Nothing changed.')
"""


