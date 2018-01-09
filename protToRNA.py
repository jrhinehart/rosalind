#Inferring mRNA from Peptides

from collections import Counter

inputFile = open('/Users/jrhinehart/Downloads/rosalind_mrna.txt','r')
fileLines = inputFile.readlines()
prot_seq = fileLines[0]
translationKey = {"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V","UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V","UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A","UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A","UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D","UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E","UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G","UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"} 

c = Counter(translationKey.values())

potentials = 1

for i in prot_seq:
	if c[i] > 0:
		print "Peptide: " + i + " Possibilities: " + str(c[i])
		potentials *= c[i] 
		#print potentials
potentials *= 3
potentials = potentials % 1000000
print "Potentials modulo 1,000,000: " + str(potentials)