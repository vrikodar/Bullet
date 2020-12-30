 
#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

import os
import sys
import bcrypt
import time
from termcolor import colored

golo = '''                                                                   
    _/_/_/    _/    _/  _/        _/        _/_/_/_/  _/_/_/_/_/   
   _/    _/  _/    _/  _/        _/        _/            _/        
  _/_/_/    _/    _/  _/        _/        _/_/_/        _/         
 _/    _/  _/    _/  _/        _/        _/            _/          
_/_/_/      _/_/    _/_/_/_/  _/_/_/_/  _/_/_/_/      _/           

                    *By SxNade https://github.com/SxNade                           
                                                           '''

version = colored("V1.0", 'red')

def intro():
    print(golo)
    to = '''
    USAGE:
    #####################################
    #                                   #
    # python3 bullet.py file-name(path) #
    #                                   #
    #####################################    \n\n\n'''
    print(colored(f"[------Bullet {version}-----]" + "\n\n", 'green'))
    time.sleep(0.5)
    print(colored(f"\n\n{to}", 'white', attrs=['reverse', 'blink']))

def encrypt():
    with open(sys.argv[1], 'r') as file:
        for line in file.readlines():
            pwd = line.strip()
            enc_pass = bcrypt.hashpw(pwd.encode('ascii'), bcrypt.gensalt())
            file_write(enc_pass)
    print(colored("{succesfully encrypted passwords}", 'white', attrs=['reverse', 'blink']))
    os.remove(sys.argv[1])

def file_write(enc_pass):
    print(colored("\n\n[*] Encrypted Password written to the ps.txt File", attrs=['reverse', 'blink']))
    file = open('ps.txt', 'a')
    file.write(f"\n{enc_pass}\n")
    file.close()
    print(colored("\n[*]Contents Written of File----\n", 'red'))
    print("\n\n")

def main():
    if len(sys.argv) != 3:
        intro()
    elif os.path.exists('ps.txt') == False or os.path.exists(sys.argv[1]) == False:
        intro()
        print(colored("\n\n[*] ps.txt or given password File is missing...!!\n", 'red'))
    else:
        print(golo)
        encrypt()

main()
