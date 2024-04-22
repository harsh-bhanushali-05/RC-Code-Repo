import numpy as np
import matplotlib.pyplot as plt
mu = 0.1
sigma = 0.05
S0 = 100
T = 1
dt = 0.001
N = int(T / dt)
t = np.linspace(0, T, N)
S = np.zeros(N)
S[0] = S0
rand = np.random.normal(0, np.sqrt(dt), size=N-1)
for i in range(1, N):
    S[i] = S[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * rand[i-1])
plt.figure(figsize=(10, 5))
plt.plot(t, S, label='GBM (mu={}, sigma={})'.format(mu, sigma))
plt.title('Geometric Brownian Motion')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
