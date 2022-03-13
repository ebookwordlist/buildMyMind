import os
import re


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


poems = {}
with open('300tang.txt') as f:
    txt = f.read()
    for i in range(1, 320):
        s = "%03d" % (i)
        e = "%03d" % (i+1)
        result = find_between(txt, s, e)
        poems[i] = result


for i in range(1, 20):
    print(poems[i])
