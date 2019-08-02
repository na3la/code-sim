d = 256


def hashing(p, t, prime=101):
    lpat = len(p)  # M = len(pat)
    ltext = len(t)  # N = len(txt)
    i = 0  # i = 0
    b = 0  # j = 0
    pat = 0  # p hash val of pat
    tex = 0  # t hash val of tex
    h = 1
    num = 0

    for i in range(lpat - 1):
        h = (h * d) % prime

    for i in range(lpat):
        pat = (d * pat + ord(p[i])) % prime
        tex = (d * tex + ord(t[i])) % prime

    for i in range(ltext - lpat + 1):
        if pat == tex:
            for b in range(lpat):
                if t[i + b] != p[b]:
                    break
            b += 1
            if b == lpat:
                print('found ' + t[i:(i+lpat)])
                num += 1
                print(num)

        if i < ltext - lpat:
            tex = (d*(tex-ord(t[i])*h) + ord(t[i + lpat])) % prime

            if tex < 0:
                tex += prime
