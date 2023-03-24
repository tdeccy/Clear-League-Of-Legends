import shutil
import os
import time

os.system('cls')

print('''\nEsse script vai apenas apagar alguns logs do League of legends..\n\n''')

def sc():
    deccy7331deccy7331deccy7331deccy7331deccy7331deccy7331deccy7331deccy7331deccy7331 = os.getlogin()

    time.sleep(2)

    sr = [
        'C:/Windows/Temp',
        f'C:/Users/{deccy7331deccy7331deccy7331deccy7331deccy7331deccy7331deccy7331deccy7331deccy7331}/AppData/Local/Temp',
        'C:/ProgramData/Riot Games',
        'C:/ProgramData/Riot Games/machine.cfg',
        'C:/Riot Games/League of Legends/Config',
        'C:/Riot Games/League of Legends/Logs',
        'C:/Riot Games/League of Legends/debug.log',
        'C:/Riot Games/Riot Client/UX/natives_blob.bin',
        'C:/Riot Games/Riot Client/UX/snapshot_blob.bin',
        'C:/Riot Games/Riot Client/UX/v8_context_snapshot.bin',
        'C:/Riot Games/Riot Client/UX/icudtl.dat',
    ]

    for a7331 in sr:
        ax1 = shutil.rmtree(a7331,ignore_errors=True)
        print('Deletado  # ',a7331)
    print('\nOK')
    time.sleep(3)
    os.system('cls' )

def ft():
    cm = [
        'RiotClientServices.exe',
        'RiotClientCrashHandler.exe',
        'VALORANT.exe',
        'VALORANT-Win64-Shipping.exe',
        'LeagueCrashHandler.exe',
        'League of Legends.exe',
        'LeagueClientUx.exe',
        'LeagueClient.exe',
        'LeagueClientUxRender.exe',
    ]

    for linha in cm:
        os.system(f'taskkill /f /im {linha}')
ft()
sc()
