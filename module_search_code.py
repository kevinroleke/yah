# -*- coding: utf-8 -*-

import sys, time, random, datetime, os, pkgutil
import Parse, os, random, requests, json
from settings import c
from requests.auth import HTTPBasicAuth
import getpass

reload(sys)
sys.setdefaultencoding('utf8')


def search(user, gu, gp):
    queries = []

    #Get All Modules In The Parse Package
    modsloaded = [name for _, name, _ in pkgutil.iter_modules(['Parse'])]
    #Loop through all modules and get their search queries
    for mod in modsloaded:
        query = getattr(Parse, mod).query()
        for queryz in query:
            queries.append(queryz)

    #Select filename for temp file
    fname = str(random.randint(1000000, 9999999)) + '.txt'
    #Open temp file and write, for module_parse_code
    with open('temp/' + fname, 'w') as f:
        for query in queries:
            #Query the github api
            r = requests.get('https://api.github.com/search/code?q=user:' + user + '%20' + query.replace(" ", "%20"), auth=HTTPBasicAuth(gu, gp))
            #Parse JSON
            j = json.loads(r.text)
            #Rate limiting
            if r.status_code == 403:
                print "Rate Limited. Waiting 2.5 minutes"
                time.sleep(300)
            elif r.status_code == 401:
                print "Incorrect username or password."
                sys.exit()
            else:
                items = j['items']

            #Define a list, for urls
            titles = []
            #Check if there are no results
            if len(items) == 0:
                pass
            else:
                #Loop through search results
                for item in items:
                    #Fetch url
                    ffr = requests.get(item['url'], auth=HTTPBasicAuth(gu, gp))
                    #Turn it into json
                    ffrj = json.loads(ffr.text)
                    #Report back to the console, the files being searched
                    print "Searching File: " + ffrj['download_url']
                    #Get branch
                    branchurl = requests.get(item['repository']['branches_url'].split("{")[0], auth=HTTPBasicAuth(gu, gp))
                    branchj = json.loads(branchurl.text)
                    branch = branchj[0]['name']
                    #Append them to a list
                    titles.append(ffrj['download_url'] + "!#!#BRANCH#!#!" + branch)
            #Loop through lines and write them to the temp file
            for title in titles:
                f.write(title.encode('utf8') + "\n")
            #Don't get banned
            #time.sleep(random.randint(3, 5))
    #Pass name of temp file to next module
    return fname
