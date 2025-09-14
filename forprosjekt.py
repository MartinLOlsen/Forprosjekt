import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("https://github.com/MartinLOlsen/Forprosjekt/blob/5f387d5dbac1e2514bab0fb57be1bc19a5cd858f/skostr_hoyde.xlsx?raw=true?", header=0)

x_i = df.iloc[:, 0]
y_i = df.iloc[:, 1]
#print(x_i)
#print(y_i)

a, b = np.polyfit(x_i, y_i, 1)
print(f'Regresjonslinje: y={a:.4f}x + {b:.4f}')

regresjonslinje = a * x_i + b
print(regresjonslinje)

plt.grid(True, zorder=0)
plt.scatter(x_i, y_i, label='Data', zorder=2)
plt.plot(x_i, regresjonslinje, color='red', label='Regresjonlinje', zorder=3)
plt.title("Python kode for forprosjekt")
plt.xlabel("Sko størrelse")
plt.ylabel("Høyde")
plt.legend()
plt.show()