#import csv
#file_to_open='Resources\election_results.csv'
#election_data = open(file_to_open, 'r')
#with open(file_to_open) as election_data:
 #   print(election_data)

import csv
import os

#Assign a variable for file to open and read
file_to_open=os.path.join("Resources", "election_results.csv")
#Assign a variable for results file to save
file_to_save=os.path.join("Analysis","election_analysis.txt")

#Open the election results file in order to read it
with open(file_to_open) as election_data:

    #To do: Read and analyze the data here
    file_reader=csv.reader(election_data)

    #Print each row in the csv file
    #for row in file_reader:
        #print(row)
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
