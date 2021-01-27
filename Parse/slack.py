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
    query = ["xoxp", "xoxb", "xoxa"]
    return query

def parse(txt, title, ln, ol, branch):
    if 'xoxp' in txt or 'xoxb' in txt or 'xoxa' in txt:
        #Test for example tokens
        if 'test' not in txt and 'token' not in txt:
            #Get the easy link
            ss = title.split('/')
            xx = ''
            for i in range(6, (len(ss))):
                xx += '/' + ss[i]
            easyl = 'https://github.com/' + ss[3] + '/' + ss[4] + '/blob/' + branch + xx + "#L" + str(ln)
            if 'xoxp' in txt:
                #Report
                # print bcolors.OKBLUE + "[*] Slack Module: Found Pass Token" + bcolors.ENDC
                #Get text after xoxa:
                ak = txt.split("xoxp")[1]
                #Removes spaces
                ak = ak.replace(" ", "")
                try:
                    ak = ak.split("\n")[0]
                except:
                    pass
                return["Slack Pass Token", easyl]
            elif 'xoxb' in txt:
                #Report
                # print bcolors.OKBLUE + "[*] Slack Module: Found Bot Token" + bcolors.ENDC
                #Get text after xoxa:
                ak = txt.split("xoxb")[1]
                #Removes spaces
                ak = ak.replace(" ", "")
                try:
                    ak = ak.split("\n")[0]
                except:
                    pass
                vl = "xoxb"

                return["Slack Bot Token", easyl]
            elif 'xoxa' in txt:
                #Report
                # print bcolors.OKBLUE + "[*] Slack Module: Found Auth Token" + bcolors.ENDC
                #Get text after xoxa:
                ak = txt.split("xoxa")[1]
                #Removes spaces
                ak = ak.replace(" ", "")
                try:
                    ak = ak.split("\n")[0]
                except:
                    pass
                vl = "xoxa"


                return["Slack Authentication Token", easyl]
            else:
                return False
        else:
            return False
    else:
        return False
