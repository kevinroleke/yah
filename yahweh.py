#!/usr/bin/env python

import random, module_parse_code, module_search_code, sys, argparse, os, socket, threading, getpass
class c:
    blue = '\033[94m'
    green = '\033[92m'
    orange = '\033[93m'
    red = '\033[91m'
    white = '\033[37m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    black = '\033[30m'

threads = []
gu = ""
gp = ""
#Telnet: Define prompt
def prompt(current_connectionz):
    current_connectionz.send("((YAHWEH))>>> ")

#Telnet: When client connects
class on_new_client(threading.Thread):
    global gu, gp
    def __init__(self, current_connectionz, addr):
        threading.Thread.__init__(self)
        self.kill_received = False
        self.current_connectionz = current_connectionz
        self.addr = addr
    def run(self):
        once = True
        current_connectionz = self.current_connectionz
        addr = self.addr
        #When client is connected, print
        print "[+] New server socket thread started for " + str(addr)

        try:
            #Login prompt
            current_connectionz.send("YAHWEH: To login, type \"LOGIN <USER> <PASS>\"\n")
        except:
            pass
        #Logged in var
        loggedin = False
        while not self.kill_received:
            #Recieve incoming data from client
            data = current_connectionz.recv(1024)
            #Debug & print data
            print data
            try:
                #If it's not a login request
                if 'LOGIN' not in data:
                    #If user has authenticated
                    if loggedin:
                        #Detect a scan order
                        if 'scan/github/user' in data:
                            #Try to start scan
                            try:
                                print data.split("scan/github/user")[1]
                                current_connectionz.send("\n[!] Starting scan on github via username\n")
                                #Start scan
                                tmp = module_search_code.search(data.split("scan/github/user ")[1].replace("\n", ""), gu, gp)
                                returnedtext = module_parse_code.parsec(tmp)
                                # print returnedtext
                                #Echo results
                                for vulnline in returnedtext:
                                    current_connectionz.send(c.green + "Found: \"" + vulnline[0] + "\" in file: " + vulnline[1] + c.end + "\n")
                                current_connectionz.send(c.end)
                                #Prompt: done
                                prompt(current_connectionz)
                            #Fall back if user not passed
                            except Exception as e:
                                print e
                                current_connectionz.send("\n[!] Please enter a github user\n")
                                prompt(current_connectionz)
                        #User typed something random, just give them another prompt
                        else:
                            prompt(current_connectionz)
                #Handle logins
                else:
                    #Test if user + pass is submitted
                    try:
                        #Test for user + pass
                        data.split(" ")[1]
                        data.split(" ")[2]
                        #Get users.
                        #TODO: Encryption
                        us = open('users', 'r').readlines()
                        #Loop through logins
                        for userpass in us:
                            #Get user + pass
                            user = userpass.split(":")[0]
                            passw = userpass.split(":")[1]
                            #Test if user exists
                            if data.split(" ")[1] == user:
                                #Test if the password is valid for the user
                                if data.split(" ")[2] == passw:
                                    #Login client
                                    current_connectionz.send("[*] Logged In: Type \"Start\"\n")
                                    loggedin = True
                                else:
                                    #Incorrect password
                                    current_connectionz.send("[:(] Failed to login\n")
                                    loggedin = False
                            else:
                                #Incorrect username
                                current_connectionz.send("[:(] Failed to login\n")
                                loggedin = False
                    #Fall back if client didn't pass a user+pass
                    except Exception as e:
                        print e
                        current_connectionz.send("[!] Please enter a user and pass\n")
            #Someone most likely quit :(
            except Exception, e:
                print "Socket Error"
                break
        current_connectionz.close()

#Start socket server
def socketserver(port):
    #Define socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Bind to a port. Changable to localhost
    s.bind(("0.0.0.0", port))
    #Change this for more max connections
    s.listen(5)
    try:
        while True:
            #Accept new connections
            (current_connection, (ip,port)) = s.accept()
            #Start thread with new client
            thread = on_new_client(current_connection, ip)
            #Add threads to list
            threads.append(thread)
            #Start thread
            thread.start()
    except KeyboardInterrupt:
        #Telnet: Ugly killall threads, if server is shutdown
        os._exit(0)
parser = argparse.ArgumentParser()

parser.add_argument('--user', '-u', dest='user', help='Specify User')

parser.add_argument('--telnet', '-t', dest='telnet', help='Server Enviorment. Telnet in, to control.', action='store_true')

parser.add_argument('--output', '-o', dest='output', help='Output to a file.')

args = parser.parse_args()


#1 in 20 chance for satanic edition
chance = 20

rando = random.randint(1,chance)

style = ""

if rando == 1:
    #Satanic Edition
    style = c.red
else:
    #Normal
    style = ""


#Ascii Art
print style + "           (`-')  _  (`-').->     .->    (`-')  _ (`-').-> "
print "     .->   (OO ).-/  (OO )__  (`(`-')/`) ( OO).-/ (OO )__  "
print " ,--.'  ,-./ ,---.  ,--. ,'-',-`( OO).',(,------.,--. ,'-' "
print "(`-')'.'  /| \ /`.\ |  | |  ||  |\  |  | |  .---'|  | |  | "
print "(OO \    / '-'|_.' ||  `-'  ||  | '.|  |(|  '--. |  `-'  | "
print " |  /   /)(|  .-.  ||  .-.  ||  |.'.|  | |  .--' |  .-.  | "
print " `-/   /`  |  | |  ||  | |  ||   ,'.   | |  `---.|  | |  | "
print "   `--'    `--' `--'`--' `--'`--'   '--' `------'`--' `--' " + c.end

#Check if telnet is specified
if args.telnet:
    #Get server ip address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    port = ""
    #Get Github account
    gu = raw_input("Github Username (not stored): ")
    gp = getpass.getpass("Github Password (not stored): ")
    if style == c.red:
        print style + "[*!*] Listening on port: 6666" + c.end
        print style + "Run nc "+ip+" 6666" + c.end
        port = 6666
    elif style == "":
        print "[*!*] Listening on port: 2018"
        print u"Run nc "+ip+" 2018"
        port = 2018
    socketserver(port)

#Get github user to scrape
user = args.user

if user:

    print style + "--------------------------------------------"
    print
    print "-    =============="+c.end+c.blue+"YAHWEH"+c.end+style+"==============    -"
    print "-             Test open sourced            -"
    print "-             repos for exposed            -"
    print "-                credentials!              -"
    print "-    =============="+c.end+c.blue+"YAHWEH"+c.end+style+"==============    -"
    print
    print "--------------------------------------------" + c.end

    #Get Github account

    gu = raw_input("Github Username (not stored): ")
    gp = getpass.getpass("Github Password (not stored): ")

    #Call modules

    tmp = module_search_code.search(user, gu, gp)

    returned = module_parse_code.parsec(tmp)

    if args.output:
        with open(args.output, 'w') as f:
            for vulnline in returned:
                f.write("Found: \"" + vulnline[0] + "\" in file: " + vulnline[1] + "\n")

else:
    print "[!] Please provide a user, using  the -u argument"

# print returned
