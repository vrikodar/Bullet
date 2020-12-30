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
    ##############################
    #                            #
    # python3 bullet.py password #
    #                            #
    ##############################    \n\n\n'''
    print(colored(f"[------Bullet {version}-----]" + "\n\n", 'green'))
    time.sleep(0.5)
    print(colored(f"\n\n{to}", 'white', attrs=['reverse', 'blink']))

def encrypt():
    global enc_pass
    enc_pass = bcrypt.hashpw(sys.argv[1].encode('ascii'), bcrypt.gensalt())
    file_write()

def file_write():
    print(colored("\n\n[*] Encrypted Password written to the ps.txt File", attrs=['reverse', 'blink']))
    file = open('ps.txt', 'w')
    file.write(f"\n{enc_pass}\n")
    file.close()
    print(colored("\n[*]Displaying Contents of File----\n", 'red'))
    os.system('cat ps.txt')
    print("\n\n")

def main():
    if len(sys.argv) != 2:
        intro()
    elif os.path.exists('ps.txt') == False:
        intro()
        print(colored("\n\n[*] ps.txt File is missing...!!\n", 'red'))
    else:
        print(golo)
        encrypt()

main()
