import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
N_MAX = 500                # Número máximo de pontos por repetição
STEP = 10                  # Incremento no tamanho da amostra
NUM_REPETICOES = 10        # Quantas repetições para cada tamanho de amostra

# Listas para armazenar os resultados
tamanhos_amostra = []           # Valores de n (tamanho da amostra)
estimativas_pi = []             # Média do π estimado para cada n
desvios_pi = []                 # Desvio padrão do π estimado para cada n

# Loop sobre diferentes tamanhos de amostra (n)
for n in np.arange(1, N_MAX, STEP):
    estimativas_para_n = []      # Armazena as 10 estimativas de π para este n
    
    # Realiza NUM_REPETICOES repetições para o mesmo n
    for _ in range(NUM_REPETICOES):
        pontos_dentro_circulo = 0
        
        # Gera n pontos aleatórios no quadrado [0,1] x [0,1]
        for _ in range(n):
            x = np.random.uniform(0, 1)
            y = np.random.uniform(0, 1)
            # Verifica se o ponto está dentro do círculo de raio 1
            if x**2 + y**2 < 1:
                pontos_dentro_circulo += 1
        
        # Estimativa de π para esta repetição: 4 * (pontos dentro / total pontos)
        pi_estimado = 4 * pontos_dentro_circulo / n
        estimativas_para_n.append(pi_estimado)
    
    # Calcula média e desvio padrão das 10 estimativas para este n
    media_pi = np.mean(estimativas_para_n)
    desvio_pi = np.std(estimativas_para_n)
    
    # Armazena os resultados
    tamanhos_amostra.append(n)
    estimativas_pi.append(media_pi)
    desvios_pi.append(desvio_pi)

plt.figure(figsize=(8, 6))
plt.errorbar(tamanhos_amostra, estimativas_pi, yerr=desvios_pi,fmt='.-b', capsize=3, label='Estimativa de π')
plt.axhline(y=np.pi, color='r', linestyle='-', label='Valor verdadeiro de π')
plt.xlabel("Número de pontos aleatórios (n)", fontsize=14)
plt.ylabel("π estimado", fontsize=14)
plt.title("Convergência do método de Monte Carlo para estimar π", fontsize=16)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()