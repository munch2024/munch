from JadonLoi_authorsFileTouches import getProcessedData
import datetime
import matplotlib.pyplot as plt
data = getProcessedData()


authors = list(author[0] for file in data.values() for author in file)
start_date = min(list(author[1] for file in data.values() for author in file))

x, y, colors = [], [], []
for i, (file, commits) in enumerate(data.items()):
    # x.append([i] * len(commits))
    x.extend([i] * len(commits))
    for author, date in commits:
        y.append((date - start_date).days // 7)
        colors.append(ord(author[0]) - ord('a'))

plt.scatter(x,y,s=10, c=colors)
plt.show()
