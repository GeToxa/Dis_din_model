


from Config import list_time_of_work, new_data
from Graphics import data_graphics


# Перезаписываем переменые

data_of_scaning = new_data  # Данные с датчиков
data_of_time = list_time_of_work    # Время записи этих данных

data_graphics(data_of_time, new_data)

