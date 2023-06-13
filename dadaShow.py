import csv

# Specify the path to the CSV file
csv_file = 'dados.csv'

# Specify the word you want to remove
word_to_remove = 'imagem'

# Read the CSV file and remove the word
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    data = list(csv_reader)
    for row in data:
        if len(row) > 0:  # Check if the row is not empty
            row[0] = row[0].replace(word_to_remove, '')  # Modify the 'tweet' column

# Overwrite the CSV file with the updated data
with open(csv_file, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
