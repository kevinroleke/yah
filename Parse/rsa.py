#RSA Module for YAHWEH - xd

#Janky import os
import re, sys, os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from settings import c

#Supply queries for the scraper
def query():
    query = ["BEGIN RSA PRIVATE KEY", "END RSA PRIVATE KEY"]
    return query

def parse(txt, title, ln, ol, branch):
    #Search for RSA headers
    if 'BEGIN RSA PRIVATE KEY' in txt or 'END RSA PRIVATE KEY' in txt:
        #Get the easy link
        ss = title.split('/')
        xx = ''
        for i in range(6, (len(ss))):
            xx += '/' + ss[i]
        easyl = 'https://github.com/' + ss[3] + '/' + ss[4] + '/blob/' + branch + xx + "#L" + str(ln)
        #Report
        #Pass back to the parser
        return ["RSA/SSH Private Key", easyl]
    else:
        return False
