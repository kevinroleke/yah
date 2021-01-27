import sys, os, re
import Parse, pkgutil, requests
from settings import c

#Remove dupes from a list
def rdupe(duplicate):
    final_list = []
    for arr in duplicate:
        if arr not in final_list:
            final_list.append(arr)
    return final_list

#Remove RSA dupes
def rsadupe(duplicate):
    final_list = []
    filelist = []
    for arr in duplicate:
        if "RSA" in duplicate:
            if arr[1].split("#")[0].split("/")[6] not in filelist:
                filelist.append(arr[1].split("#")[0].split("/")[6])
                final_list.append(arr)
                print arr[1].split("#")[0].split("/")[6]
        else:
            final_list.append(arr)
    return final_list

def parsec(tempfile):
    #Recieve temp file
    print c.underline + "Got Temp File: " + tempfile + " - Parser" + c.end
    #Open temp file
    fileUnlisted = open("temp/" + tempfile, 'r')
    text2parse = fileUnlisted.readlines()

    vulnlines = []

    maybayez = []

    #Loop through urls
    for txt in text2parse:
        #Get branch
        branch = txt.split('!#!#BRANCH#!#!')[1].replace("\n", "")
        txt = txt.split('!#!#BRANCH#!#!')[0]
        #Store fileurl
        fileurl = txt
        #Grab the url contents
        txt = requests.get(txt.replace("\n", ""))
        txt = txt.text
        #Start looping through all modules and execute them
        i = 0
        modsloaded = [name for _, name, _ in pkgutil.iter_modules(['Parse'])]
        #Split by lines
        linen = txt.split("\n")
        #Loop through lines
        for l in linen:
            #Get line numbers
            ln = i + 1
            #Get the easy link
            ss = fileurl.replace("\n", "").split('/')
            xx = ''
            for iii in range(6, (len(ss))):
                xx += '/' + ss[iii]
            easyl = 'https://github.com/' + ss[3] + '/' + ss[4] + '/blob/' + branch + xx + "#L" + str(ln)
            #Maybe an API token. Doesn't deserve it's own module
            if 'API' in l or 'apiKey' in l or 'APIKEY' in l or 'api_key' in l or 'api_token' in l or 'SECRET_KEY' in l or 'API_KEY' in l:
                if fileurl.replace("\n", "") not in maybayez:
                    print c.orange + "Maybe: Found API key(s) in file: " + easyl
                    maybayez.append(fileurl.replace("\n", ""))
            #Loop through modules
            for mod in modsloaded:
                #Grab previous and future lines, to help stop false positives
                otherLines = ""
                for z in range(2):
                    try:
                        otherLines += linen[i + (z + 1)]
                    except:
                        pass
                #Call modules
                queries = getattr(Parse, mod).query()
                res = getattr(Parse, mod).parse(l, fileurl.replace("\n", ""), ln, otherLines, branch)
                #Put results in an array
                if res:
                    vulnlines.append(res)
            i += 1
    #Remove dupes
    vulnlines = rdupe(vulnlines)
    vulnlines = rsadupe(vulnlines)
    #Report findings
    for vulnline in vulnlines:
        print c.green + "Found: \"" + vulnline[0] + "\" in file: " + vulnline[1] + c.end
    #Remove tempfile
    os.system('rm -r \"temp/' + tempfile + "\"")
    #Return results to the main file
    return vulnlines
