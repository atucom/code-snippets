#!/usr/bin/env python3

import ipdb

for i in range(1,10):
    ipdb.set_trace()
    print(i)


#also, more useful sometimes:

from IPython import embed
for i in range(1,10):
    embed()
    print(i)