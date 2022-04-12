import numpy as np


a = np.arange(25).reshape(5,5)
b = np.arange(2,27).reshape(5,5)
c = a @ b

print(a)
print('''''''''''')
print(b)
print('''''''''''')
print(c)

