import numpy as np

def StrassensMatrixMultiplication(a, b):
    if len(a) == 1: return a * b

    ar, ac = map(lambda x: x // 2, a.shape)
    a11, a12, a21, a22 = a[:ar, :ac], a[:ar, ac:], a[ar:, :ac], a[ar:, ac:]
    br, bc = map(lambda x: x // 2, b.shape)
    b11, b12, b21, b22 = b[:br, :bc], b[:br, bc:], b[br:, :bc], b[br:, bc:]

    d1 = StrassensMatrixMultiplication(a11 + a22, b11 + b22)
    d2 = StrassensMatrixMultiplication(a21 + a22, b11)
    d3 = StrassensMatrixMultiplication(a11, b12 - b22)
    d4 = StrassensMatrixMultiplication(a22, b21 - b11)
    d5 = StrassensMatrixMultiplication(a11 + a12, b22)
    d6 = StrassensMatrixMultiplication(a21 - a11, b11 + b12)
    d7 = StrassensMatrixMultiplication(a12 - a22, b21 + b22)

    c11, c12, c21, c22 = (d1 + d4 - d5 + d7), (d3 + d5), (d2 + d4), (d1 + d3 - d2 + d6)
    c = np.zeros((ar * 2, bc * 2))
    cr, cc = map(lambda x: x // 2, c.shape)
    c[:cr, :cc], c[:cr, cc:], c[cr:, :cc], c[cr:, cc:] = c11, c12, c21, c22

    return c


a = np.array([np.random.randint(10, 20) for i in range(64)]).reshape(8, 8)
b = np.array([np.random.randint(1, 10) for i in range(64)]).reshape(8, 8)
print("a =  ")
print(a)
print()
print("b = ")
print(b)
print()
print("a * b = ")
print(StrassensMatrixMultiplication(a, b))
