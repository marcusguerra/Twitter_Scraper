# Importing the os module
import os

# Directory containing the text files
directory = "C:\Users\cotoq\OneDrive\Área de Trabalho\VAI_SE_FUDER_MUSK"

# Output file name
output_file = "C:\Users\cotoq\OneDrive\Área de Trabalho\VAI_SE_FUDER_MUSK\keste.txt"

# Get the list of files in the directory
file_list = [file for file in os.listdir(directory) if file.startswith("texto_")]

# Sort the file list numerically
file_list.sort(key=lambda x: int(x.split("_")[1]))

# Open the output file in append mode
with open(output_file, "a") as outfile:
    # Iterate over the files
    for file_name in file_list:
        # Open each file in read mode
        with open(os.path.join(directory, file_name), "r") as infile:
            # Read the content and write it to the output file
            outfile.write(infile.read())
