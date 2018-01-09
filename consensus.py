# Profiling and Consensus strings

import numpy as np

inputFile = open('/Users/jrhinehart/Downloads/rosalind_cons (1).txt','r').readlines()

sequences = {}
sequence_Matrix = []
profileMatrix = []
stringLength = 0
consensusString = ''

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

fileRead(inputFile,sequences)

def seqListToMatrix(seq_List):
	stringLength = max([len(x) for x in seq_List.values()])
	output_Matrix = np.chararray([len(seq_List),stringLength])
	matrix_row=0
	for i in seq_List.keys() : 
		currentString = seq_List[i]
		#print currentString
		for nt in range(0,len(currentString)):
			output_Matrix[matrix_row,nt] = currentString[nt]
		matrix_row += 1
	print "Sequence List ingested into Matrix"
	return output_Matrix

sequence_Matrix = seqListToMatrix(sequences)

#TODO - Parse columns into Profile Matrix
def generateProfile(input_Matrix):
	locus = 0
	rowLength = len(input_Matrix[0])
	tempMatrix = np.zeros(shape=(4,rowLength))
	while locus < rowLength:
		#print input_Matrix
		#locusCount = [G,C,A,T]
		locusCount = [0,0,0,0]
		keyDict = {"G":0,"C":1,"A":2,"T":3}
		#Build locusCount
		for seq in input_Matrix :
			currentNt = seq[locus]
			locusCount[keyDict[currentNt]] += 1
		#Translate locusCount to Profile
		for row in range(0,4):
			tempMatrix[row][locus] = locusCount[row]
		#Add Nt to Consensus string?
		locus += 1
	return tempMatrix

profileMatrix = generateProfile(sequence_Matrix)
print "Profile Matrix generated"

#TODO - Generate Consensus string based on Profile
def generateConsensus(profile):
	consensusCounts = profile.argmax(axis=0)
	#print consensusCounts
	tempString = ''
	backwardsKeyDict = {0:"G",1:"C",2:"A",3:"T"}
	for n in consensusCounts:
		tempString += backwardsKeyDict[n]
	return tempString

consensusString = generateConsensus(profileMatrix)

print consensusString
print profileMatrix

outputFile = open('/Users/jrhinehart/Documents/workspace/Rosalind/stronghold/consensus_output.txt','w')
outputFile.write(consensusString + "\n")
outputFile.write("A:" + str(profileMatrix[2]).replace(".","").replace("[","").replace("]","").replace("\n","") + "\n")
outputFile.write("C:" + str(profileMatrix[1]).replace(".","").replace("[","").replace("]","").replace("\n","") + "\n")
outputFile.write("G:" + str(profileMatrix[0]).replace(".","").replace("[","").replace("]","").replace("\n","") + "\n")
outputFile.write("T:" + str(profileMatrix[3]).replace(".","").replace("[","").replace("]","").replace("\n","") + "\n")
#BUG - Newlines added inside Nucleotide specific profiles, need to remove from outputFile
print "A: " + str(profileMatrix[2]).replace(".","").replace("[","").replace("]","").replace("\n","")
print "C: " + str(profileMatrix[1]).replace(".","").replace("[","").replace("]","").replace("\n","")
print "G: " + str(profileMatrix[0]).replace(".","").replace("[","").replace("]","").replace("\n","")
print "T: " + str(profileMatrix[3]).replace(".","").replace("[","").replace("]","").replace("\n","")
outputFile.close()
