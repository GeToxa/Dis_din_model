import matplotlib.pyplot as plt
import numpy as np

from Config import  list_time_of_work, new_data

def data_graphics(list_time_of_work, new_data):
       fig, ax = plt.subplots()
       ax.stem(list_time_of_work, new_data)
       ax.plot(list_time_of_work, new_data)

       ax.set(xlabel='Время в с', ylabel='Деформация в мм',
              title='График деформаций пролетного строения')
       ax.grid()

       fig.savefig("График деформаций пролетного строения.png")
       plt.show()

