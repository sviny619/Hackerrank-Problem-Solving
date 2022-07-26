# Maria plays n games of college basketball in a season. Because 
# she wants to go pro, she tracks her points scored per game 
# sequentially in an array defined as score = [s0, s1, ..., sn-1]. 
# After each game i, she checks to see if score Si breaks her record 
# for most or least points scored so far during that season.

# Given Maria's array of scores for a season of n games, find and print 
# the number of times she breaks her record for most and least points 
# scored during the season.

# Note: Assume her records for most and least points at the start of the 
# season are the number of points scored during the first game of the season.

# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/breaking-best-and-worst-records

def getRecord(s):
    highest_score = 0
    lowest_score = 0
    count_highest = 0
    count_lowest = 0
    for i in range(len(s)):
        if i == 0:
            highest_score = lowest_score = s[i]
        elif s[i] > highest_score:
            highest_score = s[i]
            count_highest += 1
        elif s[i] < lowest_score:
            lowest_score = s[i]
            count_lowest += 1
    
    return count_highest, count_lowest

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))

# new method
def breakingRecords(scores):
    
    l_h=[scores[0]]
    l_l=[]
    h_score=scores[0]
    for i in range(1,len(scores)):
        if scores[i] > h_score:
            l_h.append(scores[i])
            h_score=scores[i]
        else:
            l_h.append(h_score)
        
    for i in range(0,len(scores)):
        if scores[i] < h_score:
            l_l.append(scores[i])
            h_score=scores[i]
        else:
            l_l.append(h_score)
    
    res = [*set(l_h)] #removing duplicates from l_h and l_l
    res_l= [*set(l_l)]
    return len(res)-1,len(res_l)-1
