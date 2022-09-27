import numpy as np
import matplotlib.pyplot as plt


from Config import list_time_of_work, new_data


N = len(new_data)  # Число измерений
dNoise = 3  # Дисперсия шума
dSignal = 2     # Дисперсия сигнала
r = 0.99    # Коэффициент корреляции в модели
en = 0.1    # Дисперсия СВ в модели

# new_data истинные координаты балки

data_fr_scan = new_data + np.random.normal(0, dNoise, N)


xx = np.zeros(N) # Вектор для хранение я оценок перемещения
P = np.zeros(N) # Вектор для хранения дисперсий ошибок оценивания
xx[0] = data_fr_scan[0]
P[0] = dNoise

for i in range(1,N):
    Pe = r*r*P[i-1]+en+en
    P[i] = (Pe*dNoise)/(Pe+dNoise)
    xx[i] = r*xx[i-1]+P[i]/dNoise*(data_fr_scan[i]-r*xx[i-1])

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(10, 5))

ax1.plot(list_time_of_work, new_data)
ax1.plot(list_time_of_work, data_fr_scan)
ax1.grid(True)


ax2.plot(list_time_of_work, xx)
ax2.grid(True)

ax3.plot(list_time_of_work, P)
ax3.grid(True)
plt.show()


