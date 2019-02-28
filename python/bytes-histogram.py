#!/usr/bin/env python3
# https://gist.github.com/mrsarm/5851c45c6934eface8de
import matplotlib.pyplot as plt
import numpy as np
from sys import argv

content = bytearray(open(argv[1], 'rb').read())

freq, bins, patches = plt.hist(content, 256)
plt.xlabel("Symbol"); plt.ylabel("Frequency")
plt.grid(True)
plt.show()