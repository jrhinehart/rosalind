inputFile = open('/Users/joshr/Documents/rosalind/datasets/rosalind_rna.txt' , 'r')
fileLines = inputFile.readlines()

dataset_seq = {}    # { 'Rosalind_xxxx' : 'GATTACA' }

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

def transcribeDNAtoRNA(sequence):
    stringRNA = ''
    for i in sequence:
        if i == 'T':
            stringRNA +='U'
        else:
            stringRNA += i
    return stringRNA

def bulkTranscribe (dataset):
    for i in dataset:
        dataset[i] = transcribeDNAtoRNA(dataset[i])
        print i
        print dataset[i]

fileRead(fileLines, dataset_seq)
bulkTranscribe(dataset_seq)
