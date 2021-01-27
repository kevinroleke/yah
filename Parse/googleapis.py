#Googleapis Module for YAHWEH - xd

#Janky import of settings file
import re, sys, os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from settings import c

#Supply queries for the scraper
def query():
    query = ["https://www.googleapis.com ?key="]
    return query

def parse(txt, title, ln, ol, branch):
    #Check for google maps/other url based google keys
    if 'https://www.googleapis.com' in txt or 'https://googleapis.com' in txt:
        if '?key=' in txt:
            #Get the easy link
            ss = title.split('/')
            xx = ''
            for i in range(6, (len(ss))):
                xx += '/' + ss[i]
            easyl = 'https://github.com/' + ss[3] + '/' + ss[4] + '/blob/' + branch + xx + "#L" + str(ln)
            #Get text after ?key=
            ak = txt.split("?key=")[1]
            #Removes spaces
            ak = ak.replace(" ", "")
            try:
                #Remove newlines
                vl = ak.split("\n")[0]
            except:
                vl = ak
            #Return to parser
            return [vl, easyl]
        else:
            return False
    else:
        return False
