import matplotlib.pyplot as plt
from datetime import datetime
import datetime
import pandas as pd

# df = pd.DataFrame(data)
# read in data
data = pd.read_csv("data/file_authors.csv")

startDate = datetime.date(2015, 6, 19)

## Create a new DataFrame to store the data for plotting
plotData = {'Author': [], 'Week': [], 'Filename': []}

# Iterate through each row of the original DataFrame and extract information for plotting
for i, row in data.iterrows():
    fileDate = datetime.date(int(row['Date'][0:4]), int(row['Date'][5:7]),int(row['Date'][8:10]))      
    # Calculate the number of days between the current date and the start date
    daysDiff = (fileDate - startDate).days
    # Calculate the week number based on 7 days per week
    weekNum = (daysDiff // 7) + 1
    plotData['Author'].append(row['Author'])
    plotData['Week'].append(int(weekNum))
    plotData['Filename'].append(row['Filename'])

# Create a new DataFrame for plotting
plotDataFrame = pd.DataFrame(plotData)

# Plotting the scatterplot
for author in plotDataFrame['Author'].unique():
    authorData = plotDataFrame[plotDataFrame['Author'] == author]
    plt.scatter(authorData['Filename'], authorData['Week'], label=author, s=50)

plt.title('Author File Changes Over Weeks')
plt.xlabel('Filename')
plt.ylabel('Weeks')
plt.xticks(rotation=90)
plt.savefig('mcgowan-author-scatterplot.png')
plt.show()
