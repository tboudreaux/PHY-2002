# Implement a matched filter using cross-correlation, to recover a signal
# that has passed through a noisy channel.
import numpy as np
from scipy import signal
sig = np.repeat([0., 1., 1., 0., 1., 0., 0., 1.], 128)
sig_noise = sig + np.random.randn(len(sig))
corr = signal.correlate(sig_noise, np.ones(12), mode='same') / 12

print corr