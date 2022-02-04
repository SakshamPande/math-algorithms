

def modular_sqrt(n, p):
    #assure that n is a quadratic residue

    legender = pow(n, (p-1)//2, p)
    if legender == 0:
        return 0
    elif legender == -1:
        print(n, "is not a quadratic residue")
        return -1
    else:
        Q, S = p-1, 0
        while Q % 2 == 0:
            Q //= 2
            S += 1
        if S == 1:
            return pow(n, (p+1)//4, p)
        z = 2
        while pow(z, (p-1)//2, p) != p-1:
            z += 1

        M = S
        c = pow(z, Q, p)
        t = pow(n, Q, p)
        R = pow(n, (Q+1)//2, p)

        while t != 1:
            for i in range(1, M):
                if pow(t, 2**i, p) == 1:
                    break
            b = pow(c, 1 << (M-i-1), p)
            M = i % p
            c = pow(b, 2, p)
            t = (t*(b**2)) % p
            R = (R*b) % p

        return R

