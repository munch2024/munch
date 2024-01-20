"""Ryan-Parker_authorsFileTouches.py: This file uses the github api to retrieve
        a list of authors and dates of files that were touched in a repository"""


import json
import requests
import csv

import os

# ! not sure if I still need this function or not
# GitHub Authentication function
def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lsttoken)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        pass
        print(e)
    return jsonData, ct


def main():
    # * This makes the data directory if not already made
    if not os.path.exists("data"):
        os.makedirs("data")

    # * Leave repo the same, in order to test against the image on the assignment
    # GitHub repo
    repo = 'scottyab/rootbeer'

    # ! Must remember to uncomment tokens before running
    # !     and to comment tokens before pushing
    lstTokens = [""] # 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
    
    file = repo.split('/')[1]

    # * Initializing input file
    inputFilePath = 'data/file_' + file + '.csv'
    # Checking if input file doesn't exist, or is empty
    if os.path.isfile(inputFilePath):
        if os.path.getsize(inputFilePath) <= 1:
            print("Input file is empty!")
            exit()
    else:
        print("Input file does not exist!")
        exit()

    inputFile = open(inputFilePath, 'r')
    reader = csv.reader(inputFile)


    # * Initializing output file
    outputFilePath = 'data/authors_' + file + '.csv'
    outputFile = open(outputFilePath, 'w')
    writer = csv.writer(outputFile)
    rows = ["Filename", "Authors", "Dates"]
    writer.writerow(rows)

    # TODO: use the list of files in inputFile to acquire the authors and dates
    # TODO:     of the files when they were touched


    # * Printing to output file with actual data
    # for authorname, date in dictfiles.items():
    #     rows = [authorname, date]
    #     writer.writerow(rows)

    # inputFile.close()
    outputFile.close()


if __name__ == "__main__":
    main()