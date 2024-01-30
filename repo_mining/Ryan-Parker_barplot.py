import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('data/authors_rootbeer.csv')

# Group by author and calculate the total contributions
author_contributions = df.groupby('Author').size().reset_index(name='Contributions')

# Sort the DataFrame in descending order by contributions
author_contributions = author_contributions.sort_values(by='Contributions', ascending=False)

# Plotting the bar graph
plt.figure(figsize=(14, 10))
plt.bar(author_contributions['Author'], author_contributions['Contributions'], color='skyblue')
plt.xlabel('Authors')
plt.ylabel('Total Contributions')
plt.title('Contributions by Authors in RootBeer Project')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display the plot
plt.savefig('data/authorContributions_rootbeer.png')
