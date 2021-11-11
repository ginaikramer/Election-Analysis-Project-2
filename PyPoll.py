import csv
import os

#Assign a variable for file to open and read
file_to_open=os.path.join("Resources", "election_results.csv")
#Assign a variable for results file to save
file_to_save=os.path.join("Analysis","election_analysis.txt")

#Open the election results file in order to read it
with open(file_to_open) as election_data:

    #Read and analyze the data here
    file_reader=csv.reader(election_data)

    #Print the header row
    headers=next(file_reader)
    print(headers)



#open(file_to_save, "w")
#outfile=open(file_to_save,"w")
#outfile.write("Hello World")
#outfile.close()

#Open the file using the with statement
with open(file_to_save,"w") as txt_file:

#Write data to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")
