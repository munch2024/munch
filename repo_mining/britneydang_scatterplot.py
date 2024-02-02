
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

#file name
csv_file_path = 'data/file_rootbeer_authordate.csv' 

#lists of each column
files = []
authors = []
preDates = []

#open file
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',') #split on ,
    
    #put in each list
    for row in reader:
        files.append(row['Filename'])
        authors.append(row['Author'])
        preDates.append(row['Date'])

#get all unique files
uniqueFiles = np.unique(files)

#total them
numberOfUniqueFiles = len(uniqueFiles)

#put it in a list
xlabel = []
for numbers in range(numberOfUniqueFiles):
    xlabel.append(numbers)
#print (xlabel)
    
#split the dates from the time
dates = []
for date in preDates:
    splitDate = date.split('T')
    dates.append(splitDate[0])

#find the minimum date
minDate = min(dates)
d2 = datetime.strptime(minDate, '%Y-%m-%d')

#calculate the weeks
weeks = []
for i in dates:
    d1 = datetime.strptime(i, '%Y-%m-%d')
    weeksCalculated = (d1 - d2).days / 7
    weeks.append(weeksCalculated)

#put it in a dataframe
finalizedData = {'Author': authors, 'Week': weeks, 'Filename': files}

#find unique authors
uniqueAuthors = np.unique(authors)

#put that in a dataframe
dataDataFrame = pd.DataFrame(finalizedData)

#sort data and plot it
for author in uniqueAuthors:
    finalData = dataDataFrame[dataDataFrame['Author'] == author]
    x = finalData['Filename']
    y = finalData['Week']
    plt.scatter(x, y , label=author, s=50)

#labelling
plt.xlabel('File')
plt.xticks(np.arange(0, numberOfUniqueFiles), labels=xlabel)
plt.ylabel('Weeks')
plt.legend(bbox_to_anchor = (1.05 , 1), loc=2)
plt.tight_layout()
plt.savefig('britneydang_Scatterplot', bbox_inches='tight', dpi=300)
plt.title('Scatter Plot of Files vs Weeks')
plt.show()
