from math import log


def d(series, i, j):
    return abs(series[i] - series[j])


f = open('ananda.txt', 'r')
series = [float(i) for i in f.read().split()]
f.close()
N = len(series)
eps = float(input('Initial diameter bound: '))
dlist = [[] for i in range(N)]
n = 0  # number of nearby pairs found
for i in range(N):
    for j in range(i + 1, N):
        if d(series, i, j) < eps:
            n += 1
            print(n)

            for k in range(min(N - i, N - j)):
                dlist[k].append(log(d(series, i + k, j + k)))
f = open('lyapunov.txt', 'w')
for i in range(len(dlist)):
    if len(dlist[i]):
        print >> f, i, sum(dlist[i]) / len(dlist[i])
f.close()