def populacao(pop_a, taxa_a, pop_b, taxa_b):
    year = 0
    while pop_a < pop_b:
        pop_a += pop_a * taxa_a/100
        pop_b += pop_b * taxa_b/100
        year += 1
    return year
