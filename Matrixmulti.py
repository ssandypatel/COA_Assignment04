import numpy as np
import time
t = time.time()
n = 32
a = np.random.randint(10, size=(n, n))
print(a)
b = np.random.randint(20, size=(n, n))
print(b)
result = a.dot(b)
for r in result:
    print(r)

t = time.time()-t
print(t)
