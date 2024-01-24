import json
import requests
import csv
from collections import defaultdict
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not os.path.exists("data"):
 os.makedirs("data")

# GitHub Authentication function
def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lstTokens)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        pass
        print(e)
    return jsonData, ct

# @dictFiles, empty dictionary of files
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(dictfiles, lsttokens, repo, touched_files):
    ipage = 1  # url page counter
    ct = 0  # token counter
    
    files_ext = set()
    try:
        # loop though all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            commitsUrl = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)
    
            # break out of the while loop if there are no more commits in the pages
            if len(jsonCommits) == 0:
                break
            # iterate through the list of commits in  spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)

                filesjson = shaDetails['files']

                if 'src' in filesjson:
                    files_ext.add(filesjson.split('.')[1])
                name = shaDetails['commit']['author']['name']
                date = shaDetails['commit']['author']['date']

                file_ext = ["kt", "java", "cpp", "h", "c", "C", "cc", "cpp", 
                            "c++", "cxx", "h", 'H', "h++", "hh", "hxx", "hpp", 
                            "css", "scss", "js"]
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    if ('.' in filename):
                        ext = filename.split('.')[1]
                        if ext not in files_ext:
                            files_ext.add(ext)

                    for ext in file_ext:
                        if filename.endswith(ext):
                            touched_files[filename].append((name, datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")))
                            dictfiles[filename] = dictfiles.get(filename, 0) + 1

            ipage += 1
    except Exception as e:
        print("Error receiving data")
        exit(0)
    
    print(files_ext)
def getProcessedData():
    return touched_files

# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = [GITHUB_TOKEN]

dictfiles = dict()
touched_files = defaultdict(list)
countfiles(dictfiles, lstTokens, repo, touched_files)
print('Total number of files: ' + str(len(touched_files)))

file = repo.split('/')[1]
# change this to the path of your file
fileOutput = 'data/file_' + file + '.csv'
rows = ["Filename", "Touches"]
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)

bigcount = None
bigfilename = None
for filename, count in dictfiles.items():
    rows = [filename, count]
    writer.writerow(rows)
    if bigcount is None or count > bigcount:
        bigcount = count
        bigfilename = filename
fileCSV.close()
print('The file ' + bigfilename + ' has been touched ' + str(bigcount) + ' times.')
