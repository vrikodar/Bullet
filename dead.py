#By SxNade
#https://github.com/SxNade/Bullet.py
#CONTRIBUTE

import os
import sys
from termcolor import colored
import requests
import time
#importing the required libraries


golo = '''
                              .___.
          /)               ,-^     ^-. 
         //               /           \
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \\               \    /|\    /
          \)               \   \_/   /
                            |       |
                            |+H+H+H+|
                            \       /
                             ^-----^'''

if len(sys.argv) != 3:
    print("python3 dead.py <password-file-name(or path)> <server-url>")
    sys.exit(0)
#check for system argumenst length

dead_countdown = '''
              ..:::::::::..
           ..:::aad8888888baa:::..
        .::::d:?88888888888?::8b::::.
      .:::d8888:?88888888??a888888b:::.
    .:::d8888888a8888888aa8888888888b:::.
   ::::dP::::::::88888888888::::::::Yb::::
  ::::dP:::::::::Y888888888P:::::::::Yb::::
 ::::d8:::::::::::Y8888888P:::::::::::8b::::
.::::88::::::::::::Y88888P::::::::::::88::::.
:::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
:::::::Y88888888888P::|::Y88888888888P:::::::
::::::::::::::::888:::|:::888::::::::::::::::
`:::::::::::::::8888888888888b::::::::::::::'
 :::::::::::::::88888888888888::::::::::::::
  :::::::::::::d88888888888888:::::::::::::
   ::::::::::::88::88::88:::88::::::::::::
    `::::::::::88::88::88:::88::::::::::'
      `::::::::88::88::P::::88::::::::'
        `::::::88::88:::::::88::::::'
           ``:::::::::::::::::::''
                ``:::::::::''
                
                
                '''

already_dead = '''
                                          .""--.._
                                           []      `'--.._
                                           ||__           `'-,
                                         `)||_ ```'--..       \
                     _                    /|//}        ``--._  |
                  .'` `'.                /////}              `\/
                 /  .""".\              //{///
                /  /_  _`\\            // `||
                | |(_)(_)||          _//   ||
                | |  /\  )|        _///\   ||
                | |L====J |       / |/ |   ||
               /  /'-..-' /    .'`  \  |   ||
              /   |  :: | |_.-`      |  \  ||
             /|   `\-::.| |          \   | ||
           /` `|   /    | |          |   / ||
         |`    \   |    / /          \  |  ||
        |       `\_|    |/      ,.__. \ |  ||
        /                     /`    `\ ||  ||
       |           .         /        \||  ||
       |                     |         |/  ||
       /         /           |         (   ||
      /          .           /          )  ||
     |            \          |             ||
    /             |          /             ||
   |\            /          |              ||
   \ `-._       |           /              ||
    \ ,//`\    /`           |              ||
     ///\  \  |             \              ||
    |||| ) |__/             |              ||
    |||| `.(                |              ||
    `\\` /`                 /              ||
       /`                   /              ||
      /                     |              ||
     |                      \              ||
    /                        |             ||
  /`                          \            ||
/`                            |            ||
`-.___,-.      .-.        ___,'            ||
         `---'`   `'----'`
         '''

print(dead_countdown + "\n\n")
print(colored("STARTING DEAD-MAN SWITCH IN 30 SECONDS...", 'red', attrs=['reverse', 'blink', 'bold']))
print("[*]Hit Contorl+C to cancel")

#setting the countdown time
time.sleep(30)

print(colored("\nSWITCH IS ACTIVE NOW!\n", 'red', attrs=['bold']))
print(golo)

try:
    while True:
        time.sleep(5)
        #make a get request to file url(server) given by the user
        r = requests.get(sys.argv[2])
        #check for status code that is if the file exists on the server or not
        if r.status_code == 200:
            print(colored("OK", 'green'))
            pass
        else:
          #if the file was not found
            print(colored("[*]SWITCH TRIGGERRED!", 'red', attrs=['reverse', 'blink']))
            #running the bullet.py script to encrypt the file contents
            os.system(f"python3 bullet.py {sys.argv[1]} {sys.argv[2]}")
            print(already_dead)
            sys.exit(0)
except KeyboardInterrupt:
  #Avoiding keyboard interrupt errors to be displayed on screen (CLEAN!!)
    print(colored("Exiting CountDown....!!", 'red', attrs=['reverse', 'blink']))
    sys.exit(0)
