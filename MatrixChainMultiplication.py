from sys import maxsize as inf
import numpy as np

#p = t, n = w, m = p, s = z, q = x,l = v

def matrixchain(t, w):
    p = [[0 for i in range(w + 2)] for i in range(w + 2)]
    z = [[0 for i in range(w + 2)] for i in range(w + 2)]

    for v in range(2, w + 1):
        for i in range(1, w - v + 2):
            j = i + v - 1
            p[i][j] = inf
            for k in range(i, j):
                x = p[i][k] + p[k + 1][j] + t[i - 1] * t[k] * t[j]
                if x < p[i][j]: p[i][j], z[i][j] = x, k

    return p, z


def multiply(A, z, i, j):
    if i < j:
        X = multiply(A, z, i, z[i][j])
        Y = multiply(A, z, z[i][j] + 1, j)
        return matrixmultiplication(X, Y)
    return A[i]

    pass


def matrixmultiplication(a, b):
    c = [[0 for i in range(len(b[0]))] for i in range(len(a))]

    for i in range(len(a)):

        for j in range(len(b[0])):

            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    return c


t = [3, 2, 2, 3]
p, z = matrixchain(t, 3)
print(np.array(p))
print(np.array(z))

A = [

    [
        [3, 4],
        [3, 4],
        [3, 4]
    ],

    [
        [3, 4],
        [3, 4]
    ],

    [
        [3, 4, 5],
        [3, 4, 5]
    ]

]
print(np.array(multiply(A, z, 0, 2)))
print(np.array(A[0]).dot(A[1]).dot(A[2]))
