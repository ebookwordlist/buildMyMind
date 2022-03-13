import os

import string

t = string.ascii_lowercase[:26]
a = list(t)

for k in a:
    print(k)
    os.system(
        "cat 1000verb.txt | grep ^{} | xargs -I{} swift ../test.swift {} > ./{}/mac_{}.md".format(k, k, k))
