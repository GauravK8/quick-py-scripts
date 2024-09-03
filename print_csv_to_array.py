import csv

# Initialize an empty list to store the data
data = []

# Open the CSV file
with open('~/csv-files/in.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV
    for row in reader:
        # Convert each element in the row to a number and append to the data list
        data.append([int(cell) if cell.isdigit() else float(cell) if cell.replace('.','',1).isdigit() else cell for cell in row])

# Print the 2D array
for row in data:
    print(row)
