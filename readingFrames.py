#!/usr/bin/python

import sys

inputFile = open(str(sys.argv[1]),'r').readlines()
sequences = {}

def fileRead(fileContentAsList, output_set):
    currentKey = ''
    for line in fileContentAsList:
        if line[0] == '>' :
            newKey = line[1:].replace('\n','')
            output_set[newKey] = ''
            currentKey = newKey
        else:
            output_set[currentKey] += line.replace('\n','')
    print "FASTA Data ingested into Sequence List "
    print "Number of Rows: " + str(len(output_set))
    return output_set

fileRead(inputFile, sequences)
print str(sequences)