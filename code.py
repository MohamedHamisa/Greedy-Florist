def getMinimumCost(k, c):
    c.sort(reverse=True)
    total_cost = 0
    for i in range(len(c)):
        total_cost += (i // k + 1) * c[i]
    return total_cost

