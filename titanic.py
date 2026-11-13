import pandas as pd  #подключаем pandas для работы с таблицами
import matplotlib.pyplot as plt  #подключаем matplotlib для графиков
a = pd.read_parquet('titanic.parquet')  #читаем исходный файл parquet в переменную a
a.to_csv('titanic.csv', index=False)  #сохраняем таблицу a в csv, index=False чтобы не было лишних номеров строк
print("Файл titanic.csv успешно сохранен.")  #пишем в консоль, что всё сохранилось
b = pd.read_csv('titanic.csv')  #читаем сохранённый csv обратно в переменную b, чтобы проверить, что файл нормальный
c = b.groupby(['Pclass', 'Survived']).size().unstack()  #группируем по классу (1,2,3) и статусу (0,1), считаем количество, разворачиваем в таблицу
c.plot(kind='bar', color=['darkred', 'green'])  #строим сгруппированную диаграмму: красный — погибшие (0), зелёный — выжившие (1)
plt.title('Выживаемость пассажиров Титаника по классам')  #заголовок графика
plt.xlabel('Класс пассажира')  #подписываем ось X
plt.ylabel('Количество человек')  #подписываем ось Y
plt.xticks(rotation=0)  #делаем подписи классов ровными, без наклона
plt.show()  #показываем график на экране