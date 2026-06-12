import numpy as np
import matplotlib.pyplot as plt

def random_num(xi, a, c, m):
    """(LCG)"""
    return (a * xi + c) % m

def main():
    n = 500
    a = 7 ** 5          
    c = 0
    m = 2**31 - 1       
    x0 = 123456789
    
    xi = x0
    X = np.zeros(n)
    X[0] = x0 / m       
    
    for i in range(1, n):
        xi = random_num(xi, a, c, m)
        X[i] = xi / m   # [0, 1)
        print(xi)

    s = np.arange(0, len(X))
    plt.figure(figsize=(8, 5))
    plt.bar(s, X, color='gray')
    plt.xlabel('n', fontsize=20)
    plt.ylabel('x', fontsize=20)
    plt.savefig('MC3.svg')
    plt.show()
    

    plt.figure(figsize=(8, 5))
    plt.hist(X, bins='auto', color='gray', histtype='bar', edgecolor='black')
    plt.xlabel('x', fontsize=20)
    plt.ylabel('P(x)', fontsize=20)
    plt.savefig('MC4.svg')
    plt.show()

if __name__ == "__main__":
    main()