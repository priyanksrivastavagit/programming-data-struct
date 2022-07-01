#!/usr/bin/env python3

import os
import logging
from datetime import datetime
import argparse

LOG_FILENAME = datetime.now().strftime(__file__+"_%d%m%Y%H%M%S.log")
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO,
    format="[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    )

class fileInitializationError(Exception):
    pass

class calculateMinimumBalanceError(Exception):
    pass

class dataQualityError(Exception):
    pass

def namedParameters(parser):
    
    parser.add_argument("-dfn", "--dataFileName",help ="Data file name")
    args = parser.parse_args()

    return args

def fileIntialization(fileName):

    '''
        Description: 
                    1. Declaring a variable to store the filename
                    2. Open the file and read all the lines except the header
        
        Input:      None

        Output:
                    1. lines:          File content excluding the header
    '''

    logging.info("Executing fileIntialization function...")

    try:

        # Assign the file name here

        #file = "minInitialBalanceAmount.csv"
        fileOpen = open(fileName)

        lines = fileOpen.readlines()[1:]

    except Exception as err:
        logging.error("Error in Opening/Reading the file:{}".format(str(err)))
        raise fileInitializationError("Error in Opening/Reading the file.")

    return lines

def intialVariableDeclaration():

    '''
        Description: 
                    1. Intitalizes all the variables
        
        Input:      None

        Output:
                    1. minBal_A:       Minimum Balance for Account "A"
                    2. minBal_B:       Minimum Balance for Account "B"
                    3. currBal_A:      Current Balance for Account "A"
                    4. currBal_B:      Current Balance for Account "B"
                    5. cntrLine:       Counter for the line number
    '''

    logging.info("Executing intialVariableDeclaration function...")

    minBal_A = 0
    minBal_B = 0
    currBal_A = 0
    currBal_B = 0
    cntrLine = 0

    return minBal_A, minBal_B, currBal_A, currBal_B, cntrLine

def calculateMinimumBalance(cntrLine, minBal_A, minBal_B, currBal_A, currBal_B, fromAccount, transferAmount):

    '''
        Description: 
                    1. Calculates the minimum balance for accounts "A" & "B".
        
        Input:      
                    1. minBal_A:       Minimum Balance for Account "A"
                    2. minBal_B:       Minimum Balance for Account "B"
                    3. currBal_A:      Current Balance for Account "A"
                    4. currBal_B:      Current Balance for Account "B"
                    5. cntrLine:       Counter for the line number
                    6. fromAccount:    Name of the account initiating the transfer
                    7. transferAmount: Transactions's transfer amount

        Output:
                    1. minBal_A:       Minimum Balance for Account "A"
                    2. minBal_B:       Minimum Balance for Account "B"
                    3. currBal_A:      Current Balance for Account "A"
                    4. currBal_B:      Current Balance for Account "B"
                    5. cntrLine:       Counter for the line number
    '''

    logging.info("Executing calculateMinimumBalance function...")

    try:

        # If reading the first record from the file, assign the minimum balance
        # as the transfer amount for the account initiating the transfer and let
        # the receiving account minimum balance assigned to 0

        if cntrLine == 0:
            logging.info("Reading the first non header line from the file.")
            if fromAccount == "A":
                minBal_A = transferAmount
                currBal_B = transferAmount
            elif fromAccount == "B":
                minBal_B = transferAmount
                currBal_A = transferAmount

            cntrLine += 1

        else:
            logging.info("Reading the second non header line onwards from the file.")
            if fromAccount == "B":
                currBal_B = currBal_B - transferAmount
                currBal_A = currBal_A + transferAmount

                # Check if the current account balance is negative after the transfer,
                # add the absolute current balance to the minimum balance to 
                # get the new minimum balance

                if currBal_B < 0:
                    minBal_B = minBal_B + abs(currBal_B)
                    currBal_B = 0
            elif fromAccount == "A":
                currBal_A = currBal_A - transferAmount
                currBal_B = currBal_B + transferAmount

                # Check if the current account balance is negative after the transfer,
                # add the absolute current balance to the minimum balance to 
                # get the new minimum balance

                if currBal_A < 0:
                    minBal_A = minBal_A + abs(currBal_A)
                    currBal_A = 0

    except Exception as err:
        logging.error("Error in calculating the minimum balance:{}".format(str(err)))
        raise calculateMinimumBalanceError("Error in calculating the minimum balance.")

    return cntrLine, minBal_A, minBal_B, currBal_A, currBal_B

def fileOperation(fileName, minBal_A, minBal_B, currBal_A, currBal_B, cntrLine):

    '''
        Description: 
                    1. This function will be used for reading the file line by 
                       line after skipping the header.
                    2. Splitting each line to extract the from and to account 
                       names and the transfer amount
        
        Input:      
                    1. minBal_A:  Minimum Balance for Account "A"
                    2. minBal_B:  Minimum Balance for Account "B"
                    3. currBal_A: Current Balance for Account "A"
                    4. currBal_B: Current Balance for Account "B"
                    5. cntrLine:  Counter for the line number

        Output:
                    1. minBal_A: Calculated minimum balance for Account "A"
                    2. minBal_B: Calculated minimum balance for Account "B"
    '''

    logging.info("Executing fileOperation function...")

    lines = fileIntialization(fileName)

    for line in lines:

        # Data quality check to the number of delimiters in the file.
        # If the number of delimiter is different than the expected value i.e. 2
        # raise an exxception and fail the job.
        
        if line.count(",") != 2:
            logging.error("Issue with the no of delimiters in the record --> {}".format(line))
            raise dataQualityError("Issue with the no of delimiters in the record --> {}".format(line))
       
        lineSplit = line.split(",")
        fromAccount = lineSplit[0]
        toAccount = lineSplit[1]
        transferAmount = int(lineSplit[2])

        cntrLine, minBal_A, minBal_B, currBal_A, currBal_B = calculateMinimumBalance(cntrLine, minBal_A, minBal_B, currBal_A, currBal_B, fromAccount, transferAmount)

    return minBal_A, minBal_B


def main():

    parser = argparse.ArgumentParser()
    args = namedParameters(parser)
    fileName = args.dataFileName

    minBal_A, minBal_B, currBal_A, currBal_B, cntrLine = intialVariableDeclaration()
    minBal_A, minBal_B = fileOperation(fileName, minBal_A, minBal_B, currBal_A, currBal_B, cntrLine)

    logging.info("Minimum Initial Account Balance for A: {}".format(minBal_A))
    logging.info("Minimum Initial Account Balance for B: {}".format(minBal_B))

    print("Minimum Initial Account Balance for A: {}".format(minBal_A))
    print("Minimum Initial Account Balance for B: {}".format(minBal_B))


if __name__ == "__main__":
    main()



