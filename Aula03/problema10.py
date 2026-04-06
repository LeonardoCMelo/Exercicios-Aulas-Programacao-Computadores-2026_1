def progressoes(a1, r, n):
    an_pa = a1 + (n - 1) * r
    an_pg = a1 * (r ** (n - 1))
    
    if an_pa > an_pg:
        sn = n * ((a1 + an_pa) / 2)
    else:
        sn = a1 * (((r ** n) - 1) / (r - 1))
    return int(sn)
