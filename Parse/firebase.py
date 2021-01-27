#Firebase Module for YAHWEH - TO

import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Supply queries for the scraper
def query():
    query = ["apiKey:", "authDomain:"]
    return query

def parse(txt, title, ln, ol, branch):

    if 'apiKey:' in txt:
        #Make sure it's a firebase init object, not a false positive
        if 'authDomain' in ol or 'databaseURL' in ol:
            if 'test' not in txt and 'API' not in txt and 'token' not in txt and 'xxx' not in txt:
                #Get the easy link
                ss = title.split('/')
                xx = ''
                for i in range(6, (len(ss))):
                    xx += '/' + ss[i]
                easyl = 'https://github.com/' + ss[3] + '/' + ss[4] + '/blob/' + branch + xx + "#L" + str(ln)
                #Get text after apiKey:
                ak = txt.split("apiKey:")[1]
                #Removes spaces
                ak = ak.replace(" ", "")
                try:
                    ak = ak.split("\n")[0]
                except:
                    pass
                #Removes qoutation marks
                vl = re.findall('"([^"]*)"', ak)[0]

                return[vl.replace("\"", ""), easyl]
            else:
                return False
        else:
            return False
    else:
        return False
