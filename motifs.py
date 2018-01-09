# Locating Motifs within a strand of DNA

inputFile = open('/Users/jrhinehart/Downloads/rosalind_subs.txt','r')
fileLines = inputFile.readlines()

s = fileLines[0].replace("\n",'')
t = fileLines[1].replace("\n",'')

print s
print t
lastIndex = 0
locations = []

while lastIndex >= 0 :
	if lastIndex == 0:
		currIndex = s.find(t,lastIndex)
		if currIndex > 0 :
			locations.append(currIndex+1)
		lastIndex = currIndex
	else:
		currIndex = s.find(t,lastIndex+1)
		#print currIndex
		if currIndex > 0 :
			locations.append(currIndex+1)
		lastIndex = currIndex
print locations

#formatted for Rosalind answer
answer = ''
for i in locations:
	answer += str(i) + " "
print answer