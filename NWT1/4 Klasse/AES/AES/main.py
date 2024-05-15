def add_round_key(s, k):
    r = []
    for (a, b) in zip(s, k):
        x = []
        for (c, d) in zip(a, b):
            x.append(c ^ d)
        r.append(x)
    return r
