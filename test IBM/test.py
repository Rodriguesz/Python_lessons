import math
import os
import random
import re
import sys



#
# Complete the 'getJSONDiff' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING json1
#  2. STRING json2
#

def getJSONDiff(json1, json2):
    # Write your code here
    diff = []

    if len(json1) > len(json2):
        maior = json1
        menor = json2
    else:
        maior = json2
        menor = json1
    
    for key in maior:
        if key in menor and maior[key] != menor[key]:
            diff.append(key)
            
    return diff
        

if __name__ == '__main__':
    json1 = {"hacker":"rank","input":"output", "teste":"testado"}

    json2 = {"hacker":"ranked","input":"wrong", "teste":"testando"}

    result = getJSONDiff(json1, json2)

    print(result)
