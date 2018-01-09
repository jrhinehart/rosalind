# Hamming Distance

# Given two strings ss and tt of equal length,
# the Hamming distance between s and t, denoted dH(s,t),
# is the number of corresponding symbols that differ in s and t.

inputFile = open('/Users/jrhinehart/Downloads/rosalind_hamm.txt', 'r')
fileLines = inputFile.readlines()

s = fileLines[0].rstrip('\n')
t = fileLines[1].rstrip('\n')

dH = 0

for bp in range(0,len(s)):
    if s[bp] != t[bp] :
        dH += 1

print dH
