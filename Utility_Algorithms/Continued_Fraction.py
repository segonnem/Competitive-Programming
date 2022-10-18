from fractions import Fraction
from math import gcd, sqrt


def period_square_roots(n):

    dico = {}
    if sqrt(n) == int(sqrt(n)):
        return([int(sqrt(n)), [] ])
    else :
        a0 = int(sqrt(n))
        L = []
        bool = True
        a = a0
        b = 1
        while bool :
            (c, a2, b2) = reduction_for_period_square_roots(n, a, b)
            a = a2
            b = b2

            if dico.get((a,b)) == None :
                dico[(a,b)] = 1
                L = L + [c]
            else :
                bool = False

    return((a0, L)) # sqrt(n) = a0 + 1/(a1 + 1/(a2 +...))   returns( L = [a0,[a1,a2,...,aN]) and sequence in L[1] is repeating


def reduction_for_period_square_roots(N,a,b):
    
    d = gcd(b,N - a**2)
    X = int(b/d)
    Y = int((N-a**2)/d)
    c = 0
    while (X*sqrt(N) + X*a)/Y - c > 1 :
        c+=1
    return( c, -(X*a - c*Y), Y)  


def expansion(L) :

    if len(L) == 1:
        return(Fraction(1,L[0]))
    else :
        return(Fraction(1,L[0] + expansion(L[1:])))  #if L = [a1,a2,...,an] returns a1 + 1/(a2 + 1 /(a3 + 1/) ...)


