import math


class ShapeException(Exception):
    pass


def is_inconsistent(*vectors):
    lval = len(vectors[0])
    if sum(len(v) != lval for v in vectors):
        return True
    return False


def is_matrix(v):
    if type(v[0]) is list:
        return True
    return False


def shape(u):
    if is_matrix(u):
        return (len(u), len(u[0]))
    else:
        return (len(u), )


def vector_add(u, w):
    if len(u) != len(w):
        raise ShapeException()
    return [i+j for i, j in zip(u, w)]


def vector_sub(u, w):
    if is_inconsistent(u, w):
        raise ShapeException()
    try:
        return [i-j for i, j in zip(u, w)]
    except:
        raise ShapeException()


def vector_sum(*vectors):
    if is_inconsistent(vectors):
        raise ShapeException()
    try:
        return [sum(v[i] for v in vectors)
                for i in range(len(vectors[0]))]
    except:
        raise ShapeException()


def dot(w, y):
    if is_inconsistent(w, y):
        raise ShapeException()
    return sum(i*j for i, j in zip(w, y))


def vector_multiply(v, w):
    return [i*w for i in v]


def vector_mean(*vectors):
    theSum = vector_sum(*vectors)
    return [i/len(vectors) for i in theSum]


def magnitude(v):
    squares = sum(i**2 for i in v)
    return squares**(0.5)


def matrix_row(A, i):
    return [j for j in A[i]]


def matrix_col(A, j):
    return [A[i][j] for i in range(len(A))]


def matrix_scalar_multiply(C, a):
    return [[C[i][j]*a for j in range(len(C[0]))]
            for i in range(len(C))]


def matrix_matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ShapeException()
    return [[sum(A[i][k]*B[k][j]
            for k in range(len(A[0])))
            for j in range(len(B[0]))]
            for i in range(len(A))]


def matrix_vector_multiply(A, v):
    vMat = [[val] for val in v]
    matOut = matrix_matrix_multiply(A, vMat)
    return [matOut[i][0] for i in range(len(matOut))]
