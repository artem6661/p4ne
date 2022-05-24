#импорт библиотек
from matplotlib import pyplot #построение графиков
from openpyxl import load_workbook #чтение эксель файлов

#забираем таблицу из файла
wb = load_workbook('data_analysis_lab.xlsx')

#лист дата из файла
sheet = wb['Data']

#значения из ячейки
def getvalue(x):
    return x.value

#три столбца забираем
list_1 = list(map(getvalue, sheet['A'][1:]))
list_2 = list(map(getvalue, sheet['C'][1:]))
list_3 = list(map(getvalue, sheet['D'][1:]))

#формируем график
pyplot.plot(list_1, list_2, label="temp")
pyplot.plot(list_1, list_3, label="active")

pyplot.legend(loc='upper left')

#вывод графика
pyplot.show()

#Сначала поставить библиотеку командой "pip.exe install matplotlib"