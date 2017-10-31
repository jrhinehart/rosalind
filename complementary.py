#find complementary DNA strand

inputSeq = open('/Users/jrhinehart/Downloads/rosalind_revc.txt', 'r').readline().replace("\n","")
#inputSeq = 'AAAACCCGGT'

complements = {'A':'T',
               'T':'A',
               'C':'G',
               'G':'C'
    }
outputSeq = ''
for i in inputSeq[::-1]:
    outputSeq += complements[i]
print outputSeq


