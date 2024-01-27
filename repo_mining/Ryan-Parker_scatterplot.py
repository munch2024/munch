"""Ryan-Parker_authorsFileTouches.py: This file gets input from the file 
		authors_repoName.csv and saves a scatter plot of the data"""


import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from datetime import datetime

def read_csv(file_path):
	"""
	Reads data from a CSV file and returns a list of dictionaries.
	Each dictionary represents a row of data with column headers as keys.
	"""
	data = []
	with open(file_path, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			data.append(row)
	return data

def convert_to_weeks(date_str, min_date):
	"""
	Converts a date string to the number of weeks since a specified minimum date.
	"""
	date_object = datetime.strptime(date_str.strip(), '%Y-%m-%dT%H:%M:%SZ')
	min_date_object = datetime.strptime(min_date.strip(), '%Y-%m-%dT%H:%M:%SZ')
	return int((date_object - min_date_object).days / 7)

def main():
	# * Leave repo the same, in order to test against the image on the assignment
	# GitHub repo
	repo = 'scottyab/rootbeer'
	# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
	# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
	# repo = 'mendhak/gpslogger'

	# * Creating name and path to file
	file = repo.split('/')[1]
	inputFilePath = 'data/authors_' + file + '.csv'
	
	# Check if the input file exists and is not empty
	if os.path.isfile(inputFilePath) and os.path.getsize(inputFilePath) > 0:
		# Read data from the CSV file
		data = read_csv(inputFilePath)

		# Find the minimum date in the dataset
		min_date = min(data, key=lambda x: datetime.strptime(x['Date'].strip(), '%Y-%m-%dT%H:%M:%SZ'))['Date']

		# Initialize lists to store unique colors and authors
		unique_colors = [] # used to not duplicate colors for authors
		authors = [] # used to verify author their color
		filename_index_map = {} # used to not duplicate files in plot

		# Iterate through the data and plot each point
		for file_entry in data:
			filename = file_entry['Filename']
			author = file_entry['Author']
			dates = file_entry['Date']

			# Convert dates to weeks
			weeks = convert_to_weeks(dates, min_date)

			# Check if the author is already in the list, if not, add it with a unique color
			if author not in authors:
				authors.append(author)
				unique_colors.append(np.random.rand(3,))

			# Get the color for the current author
			color = unique_colors[authors.index(author)]

			# Check if the filename is already in the map, if not, add it
			if filename not in filename_index_map:
				filename_index_map[filename] = len(filename_index_map)

			# Get the index for the current filename
			filename_index = filename_index_map[filename]

			# Scatter plot with each file having its own x-coordinate and assigned color
			plt.scatter(filename_index, weeks, label=author, color=color)

		# Customize the plot
		plt.xlabel('file')
		plt.ylabel('weeks')

		# Set x-axis ticks as integers
		plt.xticks(np.arange(len(filename_index_map)), [str(index) for index in range(len(filename_index_map))])

		# Save the plot as an image
		plt.savefig('data/scatterplot_' + file + '.png')
	else:
		print("Input file does not exist or is empty!")

if __name__ == "__main__":
	main()
