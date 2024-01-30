import pandas as pd
import matplotlib.pyplot as plt

# Assuming your CSV data is in a file named 'data.csv'
df = pd.read_csv('data/author_rootbeer.csv')

# Count the occurrences of each author
author_counts = df['Author'].value_counts()

# Plotting the bar graph
author_counts.plot(kind='bar', color='blue')
plt.title('Author Frequency')
plt.xlabel('Author')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.savefig('data/bargraph.png', dpi=300)

# Show the bar graph
plt.show()
