import numpy as np
import cmath

def butterfly_v1_vec(X,inverse):
    # X requires to be a power of 2 and sorted by fftshift
    X = np.array(X,np.complex_)
    N =  np.size(X)
    p = np.int16(np.log2(N)) # size(N) = 2^p

    # decide if inverse or not
    b = 1 if inverse == 1 else -1

    SIMD_LENGTH = 16

    for  L in 2**np.array(range(1,p+1)):
        d = np.min([SIMD_LENGTH,np.int_(L/2)])
        for k in np.arange(0,N,L):
            for j in np.arange(0,np.int_(L/2),SIMD_LENGTH):
                kjStart = k+j
                kjEnde = k+j+d
                wz = np.multiply(np.exp(b*1J*2*np.pi*np.arange(kjStart-k,kjEnde-k)/L),X[kjStart+np.int_(L/2):kjEnde+np.int_(L/2)])
                X[kjStart+np.int_(L/2):kjEnde+np.int_(L/2)] = np.subtract(X[kjStart:kjEnde],wz)
                X[kjStart:kjEnde] = np.add(X[kjStart:kjEnde],wz)
    return X