import requests
import json
import pandas as pd

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
        print("except")
        pass
        print(e)
    return jsonData, ct

def getTouches(lsttokens, touchDict, path):
    ct = 0
    
    commitsUrl = "https://api.github.com/repos/scottyab/rootbeer/commits?path=" + path
    jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

    for commitObject in jsonCommits:
        authorName = commitObject['commit']['author']['name']   # extract author name
        commitTime = commitObject['commit']['author']['date']   # extract commit time

        if authorName in touchDict[path]:                       # if existing author on this file, add commit time to their entry
            touchDict[path][authorName].append(commitTime)      
        else:                                                   # if new author on this file, add them to the dictionary
            touchDict[path].update({authorName:[commitTime]})

# Extract touches
lstTokens = ["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"]
repo = 'scottyab/rootbeer'
fileName = 'data/file_rootbeer.csv'

touchDict = {}
touches = pd.read_csv(fileName)     # Read CSV; collected from michael-razon_CollectFiles.py
srcFiles = touches.iloc[:,0]        # name of the source files

for i in range(len(srcFiles)):      # go through each source file and collect authors and commit times
    touchDict[srcFiles[i]] = {}
    getTouches(lstTokens, touchDict, srcFiles[i])

outputFile = "data/touches_" + repo.split('/')[1] + ".csv"  # save files to a csv

dataframe = pd.DataFrame(touchDict).transpose()
dataframe.to_csv(outputFile)

# CSV structure:
#   - heading:  author names
#   - each row represents one source file
#   - each cell contains a list of times during which the given author modified the given file
