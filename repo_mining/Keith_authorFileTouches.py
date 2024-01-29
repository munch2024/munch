import json
import requests
import csv
import os


listings = []

class Author:
    def __init__ (self, author, filename, date):
        self.author = author
        self.filename = filename
        self.date = date

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
        # loop through all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            commitsUrl = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            # break out of the while loop if there are no more commits in the pages
            if len(jsonCommits) == 0:
                break
            # iterate through the list of commits in spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)
                commit_author = shaDetails['commit']['author']['name']
                commit_date = shaDetails['commit']['author']['date']
                filesjson = shaDetails['files']
                for filenameObj in filesjson:
                    filename = filenameObj['filename']

                    # check if the file has a source code extension
                    source_code_extensions = ['.py', '.java', '.cpp', '.h', '.js', '.html', '.c', '.kt']  # Add more if needed
                    if any(filename.endswith(ext) for ext in source_code_extensions):
                        dictfiles.setdefault(filename, {'Touches': 0, 'Authors': set(), 'Dates': set()})
                        dictfiles[filename]['Touches'] += 1
                        dictfiles[filename]['Authors'].add(commit_author)
                        dictfiles[filename]['Dates'].add(commit_date)

                        individual_setter = Author(commit_author, filename, commit_date)

                        listings.append(individual_setter)
                        print(f"File: {filename}, Author: {commit_author}, Date: {commit_date}")
            ipage += 1
    except:
        print("Error receiving data")

# GitHub repo
repo = 'scottyab/rootbeer'
# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise, they will all be reverted, and you will have to re-create them
# I would advise creating more than one token for repos with heavy commits
lstTokens = ["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"]

dictfiles = dict()
countfiles(dictfiles, lstTokens, repo)
print('Total number of source files: ' + str(len(dictfiles)))

file = repo.split('/')[1]
# change this to the path of your file
file_output = 'data/source_files_info_' + file + '.csv'
rows = ["Filename", "Authors", "Dates"]
file_csv = open(file_output, 'w')
writer = csv.writer(file_csv)
writer.writerow(rows)

for author in listings:
    rows = [author.filename, author.author, author.date]
    writer.writerow(rows)

file_csv.close()
