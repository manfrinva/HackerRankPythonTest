!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def findMissing(digits,new_d):
    return list(set(digits)-set(new_d))
    # return sorted(set(range(new_d[0], new_d[-1]))- set(new_d))
    # return [x for x in range(new_d[0], new_d[-1]+1) if x not in new_d]

def computeDiff(list1, list2):
    list_diff = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return list_diff
 
def missingCharacters(s):
    # Write your code here
    digits = [0,1,2,3,4,5,6,7,8,9]
    digit = []
    character = []  
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    result = ""
    for ch in s:
        if(ch.isdigit()):
            digit.append(ch)
        else:
            character.append(ch)
    new_digit = []
    new_char = []
    new_d = []
    
    for d in digit:
        new_d.append(int(d))
    new_d.sort()
    # print(new_d)
    
    new_digit = findMissing(digits,new_d)
    new_char = computeDiff(alpha, character)
    
    print(new_digit)
    
    for j in new_digit:
        result = result + str(j)
    for i in new_char:
        result = result + i
    
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
