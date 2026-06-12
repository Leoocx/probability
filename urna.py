import random
import numpy as np
import matplotlib.pyplot as plt

urna = ['B','B','B','B','B','B','P','P','P','P']
print('Urna:', urna)

vp = []    # fração de bolas brancas por simulação
sim = []   # número de simulações
Nmax = 1000

# Probabilidade teórica
valor_teorico = urna.count('B') / len(urna)
print('Valor teórico da probabilidade:', valor_teorico)

for nsim in range(1, Nmax):
    n = 0
    for _ in range(nsim):          
        posicao = random.randint(0, len(urna)-1)
        if urna[posicao] == 'B':
            n += 1
    fracao = n / nsim
    vp.append(fracao)
    sim.append(nsim)
    
    if nsim % 100 == 0:
        print(f"nsim = {nsim:4d} → fração de brancas = {fracao:.4f} (erro = {fracao - valor_teorico:+.4f})")


plt.figure(figsize=(8,6))
plt.plot(sim, vp, linestyle='-', color="blue", linewidth=2, label='Valor simulado')
plt.axhline(y=valor_teorico, color='r', linestyle='--', label='Valor teórico')
plt.ylabel("Fração de bolas brancas", fontsize=20)
plt.xlabel("Número de experimentos", fontsize=20)
plt.xlim([0.0, Nmax])
plt.ylim([0.0, 1.0])
plt.legend()
plt.show()

