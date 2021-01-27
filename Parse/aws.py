#AWS Module for YAHWEH - xd

#Janky import of settings file
import re, sys, os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from settings import c

#Supply queries for the scraper
def query():
    query = ["aws_access_key_id", "aws_secret_access_key"]
    return query

def parse(txt, title, ln, ol, branch):
    #Check for aws credentials
    if 'aws_access_key_id' in txt or 'aws_secret_access_key' in txt:
        #Make sure it's not a test key/removed key
        if 'test' not in txt and 'API' not in txt and 'token' not in txt and 'xxx' not in txt:
            #Get the easy link
            ss = title.split('/')
            xx = ''
            for i in range(6, (len(ss))):
                xx += '/' + ss[i]
            easyl = 'https://github.com/' + ss[3] + '/' + ss[4] + '/blob/' + branch + xx + "#L" + str(ln)
            try:
                #Get token from line
                try:
                    ak = txt.split("aws_access_key_id=")[1].split("\n")[0]
                except:
                    ak = txt.split("aws_access_key_id=")[1]
                #Report
                return [ak, easyl]
            except Exception, e:
                try:
                    #Get token from line
                    try:
                        ak = txt.split("aws_secret_access_key=")[1].split("\n")[0]
                    except:
                        ak = txt.split("aws_secret_access_key=")[1]
                    #Report
                    return [ak, easyl]
                except Exception, ee:
                    return False
        else:
            return False
    else:
        return False
