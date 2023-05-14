import numpy as np
import cmath

def fftshift(X):
    # X requires to be a power of 2
    N =  np.size(X)
    p = np.int16(np.log2(N))
    for n in range(0,N):
        j = 0; m = n
        for i in range(0,p):
            j = np.int16(2*j + m%2); m = np.int16(m/2)
        if (j>n):
            h = X[j]; X[j] = X[n]; X[n] = h
    
    return X

print('Indices: ',[0,1,2,3,4,5,6,7])
print('Shifted Indices: ',fftshift([0,1,2,3,4,5,6,7]))