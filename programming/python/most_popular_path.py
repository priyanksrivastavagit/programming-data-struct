##########################################################################
# Script Name: most_popular_path.py
# Description: Find the path traversed for the most number by a list of users. The data is stored in a file format with the headers, 
#              "userId,pages traversed/read"
#              Eg. 
#              c1,p1,p2,p3,p4
#              c2, p2, p4
#              c3, p1, p2, p3
#              c4, p2, p5, p6
# Version: v1.0
# Date: 30-APR-2022
##########################################################################

import os

dictOut = {}   # Creating empty dictionary to store the key:value pair
listPages = [] # Creating empty list to store the pages traversed by each user
fileName = 'most_popular_path.csv'

# Commands to store the list of pages for each user as a separate element in the list
for line in open(fileName,'r'):
    userName = line.split(',')[0]
    pathList = line.split(',')[1:]
    listPages.append(''.join(pathList).replace('\n','').replace('\r',''))


for i in listPages: # Loop through the newly created list
    if i != '':
        varCntr = 0 # Declare a variable to store the count of occurences for each pattern
        for j in range(len(listPages)):
            if i in listPages[j]: # Parse through the entire list for each element in the list, listPages and increment the counter for each occurence
                varCntr += 1 

        dictOut[str(i)] = varCntr # Store the list of pages along with the count of its occurence as key : value pair

dictSort = sorted(dictOut.items(), key = lambda x:x[1], reverse = True) # Sort the values in descending order

print("\n\n*************************************************\nMost popular path traversed --> {}\n*************************************************".format(dictSort[0][0])) # Extract the first key post sorting

