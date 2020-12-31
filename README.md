[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Python Version](https://img.shields.io/badge/python-3.6+-green)](https://www.python.org)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/SxNade)
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)](https://github.com/SxNade/Thor)
[![Update](https://img.shields.io/badge/updated-today-brightgreen)](https://github.com/SxNade/Thor/commits/main)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/SxNade)
[![Discord](https://img.shields.io/discord/591914197219016707.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://github.com/SxNade)

[![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://github.com/SxNade)

# Bullet

![Capture](https://thumbs.gfycat.com/BriskScalyDodo-size_restricted.gif)

`Bullet is a Deadman switch password Encryptor`

# INSTALLING

*to install the required dependencies run the following commands in order*

`1 chmod +x install.sh`

`2 ./install.sh`

# HOW  DOES BULLET WORK?
*Bullet comes with Two Python Scripts bullet.py and switch.py*

**Bullet.py can be run individualy with respective arguments**

`python3 bullet.py file-name(path) start`

**KEEP A NOTE THAT 3rd Argument can be anything when running bullet.py individually..It's required to just full fill the sys.argv condition(required for switch.py)**

*Bullet can be given a password-file name as argument to script and when run successfully bullet will encrypt all the passwords present in that file and write them to another file  in encrypted form*

**PLEASE KEEP A NOTE THAT AFTER SUCCESSFULL ENCRYPTION OF PASSWORDS THE ORIGINAL FILE CONTAINING UNENCRYPTED PASSWORDS WILL BE DELETED**

# INTEGRATING DEAD-MAN SWITCH

**IN ORDER TO UTILIZE BULLET AS DEAD-MAN SWITCH YOU CAN RUN A LOCAL PYTHON SERVER ON LETS SAY PORT 8080 --- AND THEN RUN switch.py with the URL of server as argument**

# RUNNING DEAD-MAN SWITCH

*WE WILL START BY RUNNING A PYTHON SERVER ON A SPECIFIC PORT LETS SAY 8080 WITH THE FOLLOWING COMMAND*

**the directory in which the python server is run has a test.txt file which will act as a trigger to our DEAD-MAN Switch**


`python -m SimpleHTTPServer 8080`

