def avg_dist_in_claster(claster, d=None, D=None, Indexes=None, k=None, precomputed=True):
    n = len(claster)
    if n <= 1:
        return 0
    I = Indexes[k]
    if precomputed:
        return sum([D[I[i]][I[j]] for j in range(1, n) for i in range(j)]) / (n * (n - 1) / 2)
    else:
        return sum([d(claster[i], claster[j]) for j in range(1, n) for i in range(j)]) / (n * (n - 1) / 2)


## C - list of clasters, X - list of centroids, d - metric, D - distances matrix, uedd if precomputed == True
def davies_bouldin_index(C, X, d=None, D=None, Indexes=None, precomputed=True):
    n = len(C)
    assert n == len(X)

    avg = lambda c, k: avg_dist_in_claster(c, d, D, Indexes, k, precomputed)

    return sum([(max([0] + [(avg(C[i], i) + avg(C[j], j)) / d(X[i], X[j]) for j in range(n) if j != i])) for i in
                range(n)]) / n


## C - list of clasters, X - list of centroids, d - metric
def dunn_index(C, X, d=None, D=None, Indexes=None, precomputed=True):
    n = len(C)
    assert n == len(X)

    avg = lambda c, k: avg_dist_in_claster(c, d, D, Indexes, k, precomputed)

    return min([d(X[i], X[j]) for j in range(n) for i in range(j)]) \
           / max([avg(c, k) for k, c in enumerate(C)])
