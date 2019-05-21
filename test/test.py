import numpy as np
import math

data = [12,23,34,435,346,5467,65]
print(len(data))
print(len(data)/2)
print(math.floor(len(data)/2))
print('----------------------')
for i in range(2, math.floor(len(data)/2)):
    print(math.floor(len(data)/i))
