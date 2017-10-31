inputFile = open('/Users/jrhinehart/Downloads/rosalind_dna (1).txt', 'r')

inputSeq = inputFile.readlines()
inputSeq[0].replace("\n","")
ntCount = {}

for N in inputSeq[0]:
    if N in ntCount:
        ntCount[N] += 1
    else:
        ntCount[N] = 1

for key, value in ntCount.items():
    print key + ' ' + str(value)

print "Formatted for rosalind form:"
print str(ntCount['A']) + ' ' + str(ntCount['C']) + ' ' + str(ntCount['G']) + ' ' + str(ntCount['T'])
