import numpy as np
import matplotlib.pyplot as plt

dados = np.genfromtxt('C:/Users/iagom/OneDrive/Área de Trabalho/data science python/Numpy/temperatura.csv', delimiter=',', skip_header=1, usecols=(0, 1))
print(dados)
dias = dados[:,0]
temperatura = dados[:,1]
media_temperatura = np.mean(temperatura)
print(f'A média da temperatura durante esses dias foi de:  {media_temperatura:.2f} graus')
array_temperatura = np.linspace(temperatura[0], temperatura[3], 100)
dias_array = np.linspace(dias[0], dias[3], 100)
plt.plot(array_temperatura, dias_array, label='Temperatura')
plt.grid()
plt.legend()
plt.show()
