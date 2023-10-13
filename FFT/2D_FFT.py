import numpy as np
import matplotlib.pyplot as plt

# membuat array 9x9
l, w = 9, 9

# membuat array 1 dimensi sepanjang 9x9
sinyal_1d = np.zeros(l * w)

# merubah betuk menjadi array 2 dimensi
sinyal_2d = np.reshape(sinyal_1d, (l, w))

# membuat 3 sinyal 2 dimensi
sinyal_2d_1 = sinyal_2d.copy()
sinyal_2d_2 = sinyal_2d.copy()
sinyal_2d_3 = sinyal_2d.copy()

# merubah ketiga sinyal berdasarkan input fungsi kotak
sinyal_2d_1[:, 5] = 1
sinyal_2d_2[:, 3:6] = 1
sinyal_2d_3[:, 1:8] = 1

# fft 2 dimensi
sinyal_fft_1 = np.fft.fft2(sinyal_2d_1)
sinyal_fft_2 = np.fft.fft2(sinyal_2d_2)
sinyal_fft_3 = np.fft.fft2(sinyal_2d_3)

# shift fft
sinyal_fft_shifted_1 = np.fft.fftshift(sinyal_fft_1)
sinyal_fft_shifted_2 = np.fft.fftshift(sinyal_fft_2)
sinyal_fft_shifted_3 = np.fft.fftshift(sinyal_fft_3)

# mutlakkan nilai agar menjadi spektrum
magnitude_spectrum_1 = np.abs(sinyal_fft_shifted_1)
magnitude_spectrum_2 = np.abs(sinyal_fft_shifted_2)
magnitude_spectrum_3 = np.abs(sinyal_fft_shifted_3)

# membuat plot ukuran 12x8
plt.figure(figsize=(12, 8))

#plot
plt.subplot(3, 2, 1)
plt.title('2D Rectangular Signal')
plt.imshow(sinyal_2d_1, cmap='Blues')
plt.colorbar()

plt.subplot(3, 2, 2)
plt.title('2D FFT of Rectangular Signal')
plt.imshow(magnitude_spectrum_1, cmap='gray')
plt.colorbar()

plt.subplot(3, 2, 3)
plt.title('2D Rectangular Signal')
plt.imshow(sinyal_2d_2, cmap='Blues')
plt.colorbar()

plt.subplot(3, 2, 4)
plt.title('2D FFT of Rectangular Signal')
plt.imshow(magnitude_spectrum_2, cmap='gray')
plt.colorbar()

plt.subplot(3, 2, 5)
plt.title('2D Rectangular Signal')
plt.imshow(sinyal_2d_3, cmap='Blues')
plt.colorbar()

plt.subplot(3, 2, 6)
plt.title('2D FFT of Rectangular Signal')
plt.imshow(magnitude_spectrum_3, cmap='gray')
plt.colorbar()

fig = plt.gcf()
fig.subplots_adjust(hspace=0.5)

plt.show()