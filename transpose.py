'''
transpose.py
'''
import sys
'''This module was imported to use the command line parameter to enter the input and output text file.'''

def transpose(matrix):

    #This creates an empty larger list for the smallers lists to be appended to.
    transposeList = []

    #This for loop will go through each list within the matrix and take the corresponding position within each smaller list and append it to a list, which will then be appended to the larger transposeList to create the new transposed list.
    for i in range(len(matrix[0])):
        alist = []
        for j in range(len(matrix)):
            value = matrix[j][i]
            alist.append(value)
        transposeList.append(alist)
    return transposeList

def main():

    #This opens the text file as a command line parameter and reads each line, assigning its content to the variable 'line'. 
    fin = open(sys.argv[1],'r')
    line = fin.readline()
    
    #This is the larger list where the smaller lists will be appended to.
    matrix = []

    #This while loop has a condition where the loop will stop when there is nothing left in the file to read.
    while line != '':
        aList = []
        #This will split the line by spaces.
        value = line.split()

        #This for loop will go through each item in value and append it to aList and after it goes through all the items, it will append aList to the larger matrix. 
        for item in value:
            aList.append(item)
        matrix.append(aList)

        #This code allows the program to move on to the next line in the text file.
        line = fin.readline()

    #This closes the text file. 
    fin.close()

    #This creates a new text file where the file name is inputed as a command line parameter.
    fout = open(sys.argv[2],'w')

    #This assigns the transposed matrix list returned from the transpose(matrix) function to a variable.
    transMatrix = transpose(matrix)

    #This nested for loop will go through, list by list, and write each item into the new text file with spaces in between each number and with each list in a new row. 
    for item in transMatrix:
        for i in range(len(item)):
            fout.write(str(item[i]) + ' ')
        fout.write('\n')

    #This closes the text file. 
    fout.close

main()
