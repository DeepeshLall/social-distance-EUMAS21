#!/usr/bin/env python

def windowSum(arr, length):
    arr = list(map(float, arr))
    curr_sum = sum(arr[:length])
    out = [curr_sum]
    for idx in range(1, len(arr)-length+1):
        curr_sum -= float(arr[idx-1])
        curr_sum += float(arr[idx+length-1])
        out.append(curr_sum)
    out = list(map(lambda x: round(x, 5),out))
    return out
