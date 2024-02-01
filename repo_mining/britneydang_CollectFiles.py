import json
import requests
import csv
import pathlib

import os

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
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter

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
            
            # testing for code source files
            sourceCodeTests = ['.cpp', '.java', '.kt', '.h']       
            
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)
                filesjson = shaDetails['files']
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    
                    #Obtain file extension
                    fileExtension = pathlib.Path(filename).suffix
                    
                    #if the file has a valid file extension
                    if fileExtension in sourceCodeTests:
                        testSrc = []
                        testSrc = filename.split('/') #split the file name
                        for i in testSrc: #find source
                            if i == "src":
                                dictfiles[filename] = dictfiles.get(filename, 0) + 1
                                print(filename)
            ipage += 1
    except:
        print("Error receiving data")
        exit(0)
# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = ["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",
                "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",
                "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"]
dictfiles = dict()
countfiles(dictfiles, lstTokens, repo)
print('Total number of files: ' + str(len(dictfiles)))

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
