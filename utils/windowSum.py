#!/usr/bin/env python

def windowSum(arr, length):
    arr = list(map(float, arr))
    curr_sum = sum(arr[:length])
    out = []
    for idx in range(0, len(arr)-length):
        out.append(curr_sum)
        curr_sum -= float(arr[idx])
        curr_sum += float(arr[idx+length])
    out = list(map(lambda x: round(x, 5),out))
    return out
