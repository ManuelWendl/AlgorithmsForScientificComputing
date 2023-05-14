import numpy as np
import cmath

def butterfly_v1_loop(X,inverse):
    # X requires to be a power of 2 and sorted by fftshift
    X = np.array(X,np.complex_)
    N =  np.size(X)
    p = np.int16(np.log2(N)) # size(N) = 2^p

    # decide if inverse or not
    b = 1 if inverse == 1 else -1

    M = 8

    for  L in 2**np.array(range(1,p+1)):
        M = np.max([M,L]) # Necessary condition
        for kb in np.arange(0,N,M):
            for k in np.arange(kb,kb+M,L):
                for j in range(0,np.int_(L/2)):
                    wz = cmath.exp(b*1J*2*cmath.pi*j/L)*X[k+j+np.int_(L/2)]
                    X[k+j+np.int_(L/2)] = X[k+j] - wz
                    X[k+j] = X[k+j] + wz
    return X