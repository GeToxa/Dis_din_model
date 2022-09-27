# На данный момент тут создаются данные, далее тут должны обрабтываться данные

import numpy as np
import random as rd

# Генерация двнных пролетного строения
# Время записи данных и значение деформации соответственно времени

time_of_work = 20*60    #Период работы датчика
data = []       # Список данных с датчика
chasti = 12     # Количество данных за период съемки

t_one_period = np.linspace(0, np.pi, chasti)    # Cписок секнд за один период съемки

def generatr_data():

    # генерация данных съемки датчика

    for i in t_one_period:

        # Создание данных распределенных по синусу

        data_of_deformation = 1 + 20 * np.sin(i)
        data.append(data_of_deformation)

    new_data = []

    for _ in range(10):

        # добавление случайных отклонений в диапозоне от 1 до 3

        sp = []
        for i in data:
            i += rd.randint(1, 7)
            sp.append(i)
        new_data += sp
    return new_data

new_data = generatr_data() # Cписок значений за полный период съемки
list_time_of_work = np.linspace(0, time_of_work, chasti*10) # Список секунд за полное время работы датчика

