import numpy as np
import matplotlib.pyplot as plt

# membuat array 16x16
l, w = 16, 16 

# membuat array 1 dimensi sepanjang 16x16
sinyal_1d = np.zeros(l * w)

# merubah betuk menjadi array 2 dimensi
input_matrix = np.reshape(sinyal_1d, (l, w))

# membuat sinyal kotak
input_matrix_1 = input_matrix.copy()
input_matrix_2 = input_matrix.copy()
input_matrix_3 = input_matrix.copy()

# merubah ketiga sinyal berdasarkan input fungsi kotak
input_matrix_1[:, 8] = 1
input_matrix_2[:, 6:9] = 1
input_matrix_3[:, 4:10] = 1

# fungsi fft
def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    factor = [np.exp(-2j * np.pi * k / N) * odd_k for k, odd_k in enumerate(odd)]
    return [even_k + twiddle_k for even_k, twiddle_k in zip(even, factor)] + \
           [even_k - twiddle_k for even_k, twiddle_k in zip(even, factor)]

def ifft(x):
    N = len(x)
    if N <= 1:
        return x
    even = ifft(x[0::2])
    odd = ifft(x[1::2])
    factor = [np.exp(2j * np.pi * k / N) * odd_k for k, odd_k in enumerate(odd)]
    return [even_k + twiddle_k for even_k, twiddle_k in zip(even, factor)] + \
           [even_k - twiddle_k for even_k, twiddle_k in zip(even, factor)]

def fft2d(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        matrix[i] = fft(matrix[i])

    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = fft(col)
        for i in range(rows):
            matrix[i][j] = col[i]
    return matrix

def ifft2d(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        matrix[i] = ifft(matrix[i])

    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = ifft(col)
        for i in range(rows):
            matrix[i][j] = col[i]
    return matrix

def fmcc(matrix):
    fft_matrix = fft2d(matrix)
    log_spectrum = np.log(np.abs(fft_matrix) ** 2 + 1e-10)
    cepstrum = ifft2d(log_spectrum)
    return cepstrum

for i in range(len(input_matrix)):
    for j in range(len(input_matrix[0])):
        input_matrix[i][j] += i + j 

fmcc_result_1 = fmcc(input_matrix_1)
fmcc_result_2 = fmcc(input_matrix_2)
fmcc_result_3 = fmcc(input_matrix_3)


plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.title("Fungsi kotak a/2")
plt.imshow(np.abs(input_matrix_1), cmap='winter')
plt.colorbar()

plt.subplot(2, 3, 4)
plt.title("FMCC1")
plt.imshow(np.abs(fmcc_result_1), cmap='Reds')
plt.colorbar()

plt.subplot(2, 3, 2)
plt.title("Fungsi kotak a")
plt.imshow(np.abs(input_matrix_1), cmap='winter')
plt.colorbar()

plt.subplot(2, 3, 5)
plt.title("FMCC2")
plt.imshow(np.abs(fmcc_result_1), cmap='Reds')
plt.colorbar()

plt.subplot(2, 3, 3)
plt.title("Fungsi kotak 3a")
plt.imshow(np.abs(input_matrix_1), cmap='winter')
plt.colorbar()

plt.subplot(2, 3, 6)
plt.title("FMCC3")
plt.imshow(np.abs(fmcc_result_1), cmap='Reds')
plt.colorbar()

plt.show()