import numpy as np
from scipy import signal
a = [10, 10, 10, 10]
b = [10, 10, 10, 10]

coef = signal.convolve(a, b)
print coef
