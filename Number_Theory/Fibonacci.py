def fibonacci(n):
  def fib_inner(n):
    '''Returns F[n] and L[n]'''
    if n == 0:
      return 0, 2
    u, v = fib_inner(n >> 1)
    q = (n & 2) - 1
    u, v = u * v, v * v + 2*q
    if (n & 1):
      u1 = (u + v) >> 1
      return u1, 2*u + u1
    return u, v

  u, v = fib_inner(n >> 1)
  if (n & 1):
    q = (n & 2) - 1
    u1 = (u + v) >> 1
    return v * u1 + q
  return u * v



'''Compute F_n in O(logn)'''

def matrix_mult(A, B):
    
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

def matrix_power(matrix, n):
    
    # Base case: The identity matrix
    result = [[1, 0], [0, 1]]
    base = matrix

    while n > 0:
        # If n is odd, multiply the base matrix with the result
        if n % 2 == 1:
            result = matrix_mult(result, base)
        # Square the matrix and halve n
        base = matrix_mult(base, base)
        n //= 2

    return result

def fibonacci(n):
    
    if n == 0:
        return 0
    # The transformation matrix
    F = [[1, 1],
         [1, 0]]
    # Raise the transformation matrix to the power of (n-1)
    result = matrix_power(F, n-1)
    return result[0][0]

print(fibonacci(10))  # Output: 55
