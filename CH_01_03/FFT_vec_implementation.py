import numpy as np
import copy

# Reindexing (Bit Reversal) Algorithm 
def fftshift(X):
    # X requires to be a power of 2
    N =  np.size(X)
    p = np.int16(np.log2(N)) # size(N) = 2^p

    for n in range(0,N):
        j = 0; m = n
        for i in range(0,p):
            j = np.int16(2*j + m%2); m = np.int16(m/2)
        if (j>n):
            h = X[j]; X[j] = X[n]; X[n] = h
    return X

def butterfly_vec(X,inverse):
    # X requires to be a power of 2 
    X = np.array(fftshift(X),np.complex_)

    N =  np.size(X)
    p = np.int16(np.log2(N)) # size(N) = 2^p

    # decide if inverse or not
    b = 1 if inverse == 1 else -1

    for  L in 2**np.array(range(1,p+1)):
        for k in np.arange(0,N,L):
            wz = np.exp(b*1J*2*np.pi*np.arange(0,np.int_(L/2))/L)*X[k+np.int_(L/2):k+L]
            X[k+np.int_(L/2):k+L] = X[k:k+np.int_(L/2)] - wz
            X[k:k+np.int_(L/2)] = X[k:k+np.int_(L/2)] + wz
    return X

def fft(X):
    return butterfly_vec(X,0)

def ifft(X):
    return 1/np.size(X)*butterfly_vec(X,1)