"""Ryan-Parker_authorsFileTouches.py: This file uses the github api to retrieve
		a list of authors and dates of files that were touched in a repository"""

# Note: This file was written with inspiration from the CollectFiles script
#           from the github repository johnxu21/msrLab


import json
import requests
import csv

import os

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

# Function to get authors and dates for each file
def get_authors_and_dates(dictfiles, lsttokens, repo):
	ct = 0  # token counter
	authors_and_dates = []

	try:
		# loop through all filenames from the input_file
		for filename in dictfiles:
			print("Getting Author(s) and Date(s) for file: " + filename)
			ipage = 1  # reset url page counter for each file

			# loop through all the commit pages until the last returned empty page
			while True:
				spage = str(ipage)
				commitsUrl = 'https://api.github.com/repos/' + repo + '/commits?path=' + filename + '&page=' + spage + '&per_page=100'
				jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

				# break out of the while loop if there are no more commits in the pages
				if len(jsonCommits) == 0:
					break

				# iterate through the list of commits in spage
				for shaObject in jsonCommits:
					sha = shaObject['sha']
					# For each commit, use the GitHub commit API to extract the author and date
					shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
					shaDetails, ct = github_auth(shaUrl, lsttokens, ct)

					# get the author and date vlues for this commit
					author = shaDetails['commit']['author']['name']
					date = shaDetails['commit']['author']['date']
					# append the filename, author, and date
					authors_and_dates.append({'Filename': filename, 'Author': author, 'Date': date})

				ipage += 1
	except:
		print("Error receiving data")
		exit(0)

	return authors_and_dates


def main():
	# * This makes the data directory if not already made
	if not os.path.exists("data"):
		os.makedirs("data")

	# * Leave repo the same, in order to test against the image on the assignment
	# GitHub repo
	repo = 'scottyab/rootbeer'
	# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
	# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
	# repo = 'mendhak/gpslogger'


	# ! Must remember to uncomment tokens before running
	# !     and to comment tokens before pushing
	# put your tokens here
	# Remember to empty the list when going to commit to GitHub.
	# Otherwise they will all be reverted and you will have to re-create them
	# I would advise to create more than one token for repos with heavy commits
	lstTokens = ["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"] # 

	# * Creating name and path to files
	file = repo.split('/')[1]
	input_file = 'data/file_' + file + '.csv'

	# read the input_file into dictfiles
	with open(input_file, 'r') as fileCSV:
		reader = csv.reader(fileCSV)
		next(reader)  # Skip header row
		dictfiles = [row[0] for row in reader]

	# Get authors and dates for each file
	authors_and_dates = get_authors_and_dates(dictfiles, lstTokens, repo)

	# Write authors output file
	output_file = 'data/authors_' + file + '.csv'
	with open(output_file, 'w', newline='') as fileCSV:
		fieldnames = ['Filename', 'Author', 'Date']
		writer = csv.DictWriter(fileCSV, fieldnames=fieldnames)

		# Write header
		writer.writeheader()

		# Write data
		writer.writerows(authors_and_dates)
	
	print('Authors and dates information saved to authors_rootbeer.csv')

if __name__ == "__main__":
	main()
