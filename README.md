[![SxNade](https://img.shields.io/badge/MadeBy-SxNade-red)

# Bullet

![Capture](https://github.com/SxNade/Bullet/blob/main/Bullet.png)

`Bullet is a Remotely Tigerrable powerful Deadman switch`

**MADE BY-SxNade**

**when Triggered**

(of --> to)

![Capture](https://github.com/SxNade/Bullet/blob/main/bullet.gif)

---

# `INSTALLING`

*to install the required dependencies run the following commands in order*

`1 chmod +x install.sh`

`2 ./install.sh`

# `HOW  DOES BULLET WORK?`

*Bullet comes with Two Python Scripts bullet.py and dead.py*

**Bullet.py can be run individualy with respective arguments**

`python3 bullet.py file-name(path) start`

**KEEP A NOTE THAT 3rd Argument can be anything when running bullet.py individually..It's required to just full fill the sys.argv condition(required for switch.py)**

*Bullet can be given a password-file name as argument to script and when run successfully bullet will encrypt all the passwords present in that file and write them to another file  in encrypted form*

**PLEASE KEEP A NOTE THAT AFTER SUCCESSFULL ENCRYPTION OF PASSWORDS THE ORIGINAL FILE CONTAINING UNENCRYPTED PASSWORDS WILL BE DELETED**

# `INTEGRATING DEAD-MAN SWITCH`

**IN ORDER TO UTILIZE BULLET AS DEAD-MAN SWITCH YOU CAN RUN A LOCAL PYTHON SERVER ON LETS SAY PORT 8080 --- AND THEN RUN dead.py with the URL of server as argument**

# `RUNNING DEAD-MAN SWITCH`

*WE WILL START BY RUNNING A PYTHON SERVER ON A SPECIFIC PORT LETS SAY 8080 WITH THE FOLLOWING COMMAND*

**the directory in which the python server is run has a test.txt file which will act as a trigger to our DEAD-MAN Switch**


`python -m SimpleHTTPServer 8080`

![Capture](https://raw.githubusercontent.com/SxNade/Bullet/main/imgs/server.png)

*the current directory also contains a file test.txt*

**NOW THAT WE HAVE OUR SERVER RUNNING WE WILL RUN OUR SCRIPT `dead.py` ALONG WITH OUR SERVER RUNNING**

*BUT BEFORE WE WILL ALSO CREATE A SIMPLE PASSWORD LIST*

![Capture](https://raw.githubusercontent.com/SxNade/Bullet/main/imgs/pass_list.png)

*I HAVE CREATED A PASSWORD LIST NAMED `pass.txt` AND NOW ITS TIME TO RUN OUR DEADMAN SWITCH*


**python3 dead.py <password-file-name(or path)> <server-url>**
  
*IN our scenario this command will be `python3 pass.txt http://192.168.0.108:8080/test.txt`*

**we will see that a timer will be displayed**

![Capture](https://raw.githubusercontent.com/SxNade/Bullet/main/imgs/count.png)

**we will not hit ctrl+c and will let the program continue**

**AFTER 30 SECONDS OF COUNTDWON**

![Capture](https://raw.githubusercontent.com/SxNade/Bullet/main/imgs/requests.png)

*WE CAN SEE FROM THE IMAGE ABOVE THAT THE SWITCH IS MAKING A HTTP GET REQUEST EVERY 5 SECONDS FOR THE `test.txt` FILE WHICH WE CREATED BEFORE*

**NOW WE WILL REMOVE THE `test.txt` FILE FROM THE PYTHON SERVER AND SEE HOW THE SWITCH REACTS TO IT**

![Capture](https://raw.githubusercontent.com/SxNade/Bullet/main/imgs/triggered.png)

*we can see that as soon as we removed the file test.txt we get a message in terminal that switch is triggered(we can also see the file not found error in server logs)*

**AFTER THE SWITCH GETS TRIGGERED FOLLOWING HAPPENS**

![Capture](https://raw.githubusercontent.com/SxNade/Bullet/main/imgs/executed.png)

**we get notified that the encrypted passwords have been written to a ps.txt file**

*NOW LETS JUST VIEW THE CONTENTS OF THE `ps.txt` FILE*

![Capture](https://raw.githubusercontent.com/SxNade/Bullet/main/imgs/enc_ps.png)

*AND ALL THE PASSWORDS ARE NOW ECRYPTED AND SAVED TO `ps.txt` FILE*

**The original file pass.txt containing the unencrypted passwords has been removed**

# `MORE_INFO`

*The capabilities of bullet can be extended from what they are right now-- that is the code can be modified to send emails to specified address before dying!*

**OR**

`IT can also act as a Triggrable ransomware`

# `ADDITIONS`

**MORE ADDITIONAL FEATURES WILL BE ADDED BULLET IN UPCOMING DAYS**


# `MAKE_IT_BETTER`

*In order to make bullet even better contribute or report any bugs or fixes required*

`git clone https://github.com/SxNade/Bullet`

