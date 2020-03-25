import matplotlib.pyplot as plt

def N(c):
    i = 0
    z = 0
    while z < 2:
        i += 1
        z = z ** 2 + c
    return i

pis = []
plt.plot(pis)
plt.show()
for i in range(100):
    epsilon = 10 ** -(2 * i)
    c = 0.25 + epsilon
    pi = N(c) * 10 ** -(len(str(N(c))) - 1)
    pis.append(pi)
    print(pi)
    plt.clf()
    plt.plot(pis)
    plt.show()