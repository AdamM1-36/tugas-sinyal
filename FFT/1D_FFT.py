from cmath import exp, pi
import matplotlib.pyplot as plt
import numpy as np

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    # recursion
    even = fft(x[0::2])
    odd = fft(x[1::2])
    # The second term in FFT equation (e^(-2j*pi*k/N) * odd part)
    q = [exp(-2j * pi * k / N) * odd[k] for k in range(N//2)]

    return \
        [ (even[k] + q[k]) for k in range(N//2)] + \
        [ (even[k] - q[k]) for k in range(N//2)]

# Define signal parameters
A = 2
def signal1(t, A):
    return 1 if -A/2 < t < A/2 else 0
def signal2(t, A):
    return 1 if -A < t < A else 0
def signal3(t, A):
    return 1 if -3*A < t < 3*A else 0

# Define plot parameters: n mus be the power of 2 because FFT algorithm using divide and conquer
t_interval = 7 * A
n = 512

# Generate time interval from -t_interval/2 to t_interval/2
t = [i * t_interval / n for i in range(-n//2, n//2)]

signal1_data = [signal1(i, A) for i in t]
signal2_data = [signal2(i, A) for i in t]
signal3_data = [signal3(i, A) for i in t]

output_1 = fft(signal1_data)
output_2 = fft(signal2_data)
output_3 = fft(signal3_data)

output_1_oneside = output_1[:n//2]
output_2_oneside = output_2[:n//2]
output_3_oneside = output_3[:n//2]


# Generate frequency interval from 0 to n/2
f = list(range(n//2))


np_output_1 = np.fft.fft(signal1_data)
np_output_2 = np.fft.fft(signal2_data)
np_output_3 = np.fft.fft(signal3_data)

np_output_1_oneside = np_output_1[:n//2]
np_output_2_oneside = np_output_2[:n//2]
np_output_3_oneside = np_output_3[:n//2]


plt.figure(figsize=(12, 8))

plt.subplot(331)
plt.plot(t, [signal1(i, A) for i in t])
plt.title('Signal 1(A/2)')

plt.subplot(332)
plt.plot(f, output_1_oneside)
plt.title('myFFT of Signal 1')

plt.subplot(333)
plt.plot(f, np_output_1_oneside)
plt.title('npFFT of Signal 1')

plt.subplot(334)
plt.plot(t, [signal2(i, A) for i in t])
plt.title('Signal 2(A)')

plt.subplot(335)
plt.plot(f, output_2_oneside)
plt.title('myFFT of Signal 2')

plt.subplot(336)
plt.plot(f, np_output_2_oneside)
plt.title('npFFT of Signal 2')

plt.subplot(337)
plt.plot(t, [signal3(i, A) for i in t])
plt.title('Signal 3(3A)')

plt.subplot(338)
plt.plot(f, output_3_oneside)
plt.title('myFFT of Signal 3')

plt.subplot(339)
plt.plot(f, np_output_3_oneside)
plt.title('npFFT of Signal 3')

fig = plt.gcf()
fig.subplots_adjust(hspace=0.4)
plt.show()
