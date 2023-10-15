# Tugas 2 PSO
## Naive Implementation of 1D Convolution
### Python script
```
def conv_1d(x, h, p, s):
    # Membuat list copy dari list agar bersifat pass-by-value
    # agar tidak terpengaruh penambahan padding
    signal = x[:]
    # Rotasi kernel
    kernel = h[::-1]

    # n = ukuran sinyal, m = ukuran kernel
    n = len(signal)
    m = len(kernel)
    
    # Tentukan ukuran output dengan formula berikut
    o = int((n+2*p-m)/s) + 1

    # Tambahkan padding
    for i in range(p):
        signal.insert(0, 0)
        signal.append(0)

    ans = []
    
    # loop untuk mengisi nilai pada tiap index output
    for i in range(0, o, s):
        temp = 0
        # loop untuk mencari nilai hasil konvolusi tiap index
        for j in range(m):
            temp += signal[i+j]*kernel[j]
        ans.append(temp)
    
    return ans

if __name__ == "__main__":
    print("Naive Implementation of Convolution")
    print("Adam Mahendra")
    print("5009211069")

    signal = [0, 1, 2, 3, 4, 5, 6]
    kernel = [0, 1, 2, 3]
    # padding sebesar n-1 biasa disebut "Full mode"
    padding = len(kernel) - 1
    # stride/pergeseran sebesar 1
    stride = 1
    print(conv_1d(signal, kernel, p= padding, s=stride))
```
### Result
![conv](../Tugas-2/tugas_konvolusi.png)
