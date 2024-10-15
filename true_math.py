from math import inf

def divide (first, second):
    if second > 0:
        res = first / second
        return res
    if second == 0:
        return float('inf')
