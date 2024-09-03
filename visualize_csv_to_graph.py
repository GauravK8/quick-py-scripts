import matplotlib.pyplot as plt
import csv
 
# Read CSV file
data = []
labels = []
 
with open('~/data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        labels.append(row[0])
        data.append(row[1])
 
# Plotting the graph
plt.plot(labels, data, color='green', marker='o')
plt.title('Data from CSV to Graph using Python')
plt.xlabel('Labels')
plt.ylabel('Data Points')
plt.show()
