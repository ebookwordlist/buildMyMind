import os 

import string

t = string.ascii_lowercase[:26]
a = list(t)
print(a)

for k in a:
    print(k)
    # os.makedirs(k)