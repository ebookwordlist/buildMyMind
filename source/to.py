import os

import string

t = string.ascii_lowercase[:26]
a = list(t)

for k in a:
    print(k)
    # commnd = "cat {}/{}.txt | xargs -I{{}} swift ./test.swift {{}} > ./{}/mac_{}.md".format(
    # k, k, k, k, k)

    commnd = "mv ./{}/mac_{}.md ./{}/mac_{}.txt".format(k, k, k, k)
    os.system(commnd)
