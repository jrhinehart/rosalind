# GC Count

inputFile = open('/Users/jrhinehart/Downloads/rosalind_gc.txt' , 'r')
fileLines = inputFile.readlines()

dataset_seq = {}    # { 'Rosalind_xxxx' : 'GATTACA' }
dataset_counts = {} # { 'Rosalind_xxxx' : [G,C,A,T,ratioGC] }

def fileRead(fileContentAsList, output_set):
    currentKey = ''
    for line in fileContentAsList:
        if line[0] == '>' :
            newKey = line[1:].replace('\n','')
            output_set[newKey] = ''
            currentKey = newKey
        else:
            output_set[currentKey] += line.replace('\n','')
    print "Data ingested into dataset_seq"
    print "Number of Rows: " + str(len(output_set))
    print "  G    C    A    T   ratioGC"

def getCounts(dataset):
    for key, sequence in dataset.items():
        print key
        dataset_counts[key] = countGC(sequence)

def countGC(sequence):
    ntCountDict = {}
    for n in sequence:
        if n in ntCountDict:
            ntCountDict[n] += 1
        else:
            ntCountDict[n] = 1
    percentGC = round((ntCountDict["G"] + ntCountDict["C"])/ float(len(sequence))*100,4)
    seq_stats = [ntCountDict["G"],ntCountDict["C"],ntCountDict["A"],ntCountDict["T"],percentGC]
    print seq_stats
    return seq_stats

def findMaxGC(counts_set):
    m = max(counts_set.iterkeys(), key=lambda k: counts_set[k])
    return str(m) + "\n" + str(counts_set[m][4])

fileRead(fileLines,dataset_seq)
getCounts(dataset_seq)
print "Sequence with highest GC Content:"
print findMaxGC(dataset_counts)
