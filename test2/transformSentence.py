#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#
def transformSentence(sentence):
    answer=sentence[0]
    prev=sentence[0]
    space = False
    for i in range(1,len(sentence)):
        if not space:
            if  sentence[i].lower() > prev.lower():
                answer+=sentence[i].upper()
            elif sentence[i].lower() < prev.lower():
                answer+=sentence[i].lower()
            else:
                answer+=sentence[i]
        else:
            answer+=sentence[i]
        space = True if sentence[i]==' ' else False
        prev = prev if space else sentence[i].lower()

    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()
