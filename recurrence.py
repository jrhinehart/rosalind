#Recurrence Relationship
#Given n months and k litter size, how many rabbit pairs will exist?
# 5,3 => 19

def Recur(n,k):
    matureSet = {1:1}
    kidSet = {1:0}
    step=1
    while step <= n:
        mature=matureSet[step]
        kids=kidSet[step]
        nextKids = (mature * k)
        nextAdults = mature + kids
        step += 1
        matureSet[step] = nextAdults
        kidSet[step] = nextKids
    return matureSet[n]
#print Recur(33,3)


# Extension of this Recurrence Relationship, but with mortality
# n = # of months
# k = # of pairs born per mating pair per month
# Given 3 month life
# TODO - parameterize life-length


def RecurAndDie(n,k):
    rabbitSets = {1:[1,0,0,0]}
    month = 1
    print 'Months: ' + str(n) + ' ' + 'Birth Rate: ' + str(k)
    print 'Month ' + str(month) + ': ' + str(rabbitSets[month])
    while month <= n :
        prevSet = rabbitSets[month]
        nextSet = [0,0,0,0]
        nextSet[0] = (prevSet[1] + prevSet[2]) * k
        nextSet[1] = prevSet[0]
        nextSet[2] = prevSet[1]
        nextSet[3] = prevSet[2]
        rabbitSets[month+1] = nextSet
        month += 1
        print 'Month ' + str(month) + ': ' + str(rabbitSets[month])
    finalSet = rabbitSets[n]
    finalCount = finalSet[0] + finalSet[1] + finalSet[2]
    return finalCount
#print RecurAndDie(6,3)

def RecurAndDie2(n,k,d):
    rabbitSets = {1:[1,0]}
    month = 1
    deathOffset = d-1
    print 'Months: ' + str(n) + ' ' + 'Birth Rate: ' + str(k) + ' ' + 'Death Rate: ' + str(d)
    print 'Month ' + str(month) + ': ' + str(rabbitSets[month])
    while month <= n:
        prevSet = rabbitSets[month]
        nextSet = [0,0]
        if (month-deathOffset) in rabbitSets:
            dyingRabbits = rabbitSets[month-deathOffset][0]
        else:
            dyingRabbits = 0
        nextSet[0] = prevSet[1] * k
        nextSet[1] = (prevSet[0] + prevSet[1]) - dyingRabbits
        rabbitSets[month+1] = nextSet
        month += 1
        print 'Month ' + str(month) + ': ' + str(rabbitSets[month])
    return rabbitSets[n][0] + rabbitSets[n][1]
print RecurAndDie2(93,1,16)
        
