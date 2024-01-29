import json
import requests
import csv

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


def countfiles(authors, dictfiles, lsttokens, repo):
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
            for shaObject in jsonCommits:
                sha = shaObject['sha']

                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)
                filesjson = shaDetails['files']
                for filenameObj in filesjson:
                    filename = filenameObj['filename']

                    # Valid paths for rootbeerlib
                    libPaths = ['rootbeerlib/src/main/java/', 'rootbeerlib/src/test/java', 'rootbeerlib/src/main/cpp']

                    # Filter for source files
                    if (any(path in filename for path in libPaths) and
                            any(filename.endswith(ext) for ext in ['.java', '.cpp', '.h', '.txt']) or
                            'app/src/main/' in filename and
                            filename.endswith('.kt')):
                        dictfiles[filename] = dictfiles.get(filename, 0) + 1

                        authorName = shaObject['commit']['author']['name']
                        commitDate = shaObject['commit']['author']['date']

                        authors.append_date(authorName, filename, commitDate)
                        print(f"Author: {authorName}, File: {filename}, Date: {commitDate}")

            ipage += 1
    except:
        print("Error receiving data")
        exit(0)


# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


class AuthorData:
    def __init__(self):
        self.attributes = {}

    def append_date(self, author, file, date):
        # Check if the author exists in the dictionary
        if author not in self.attributes:
            self.attributes[author] = {}

        # Check if the file exists in the author's dictionary
        if file not in self.attributes[author]:
            self.attributes[author][file] = []

        # Append the date to the list
        self.attributes[author][file].append(date)

    def write_to_csv(self, file_output):
        with open(file_output, 'w', newline='') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(["Author", "File", "Date"])

            for author, files in self.attributes.items():
                for file, dates in files.items():
                    for date in dates:
                        writer.writerow([author, file, date])


authors = AuthorData()


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = ["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"]

dictfiles = dict()
countfiles(authors, dictfiles, lstTokens, repo)

file = repo.split('/')[1]
# change this to the path of your file
fileOutput = 'data/author_' + file + '.csv'
authors.write_to_csv(fileOutput)
