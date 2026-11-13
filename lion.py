import docx  #подключаю библиотеку для работы с docx
from collections import Counter  #Counter пригодится для подсчёта частот
import matplotlib.pyplot as plt  #matplotlib нужен для графика

lion = docx.Document('lion.docx')  #читаю исходный документ
doc = docx.Document()  #создаю новый документ для таблицы
text = []  #сюда потом сложу текст
letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']  #список строчных русских букв для фильтрации
table = doc.add_table(rows = 1, cols = 3)  #создаю таблицу с одной строкой и тремя колонками
table.style = 'Table Grid'  #задаю стиль таблицы с границами

hdr_cells = table.rows[0].cells  #беру ячейки первой строки под заголовки
hdr_cells[0].text = 'Слово'  #заголовок первой колонки
hdr_cells[1].text = 'Частота встречи, раз'  #заголовок второй колонки
hdr_cells[2].text = 'Частота встречи, %'  #заголовок третьей колонки

text = '\n'.join([paragraph.text for paragraph in lion.paragraphs])  #собираю текст из всех абзацев в одну строку
text_lower = text.lower()  #привожу текст к нижнему регистру
words = text_lower.split()  #разбиваю текст на слова

filtered_words = [word.strip(" ,.!?()[]{}'\"-_@") for word in words if len(word) > 0 and all(char in letters for char in word.strip(" ,.!?()[]{}'\"-_@"))]  #чищу слова от знаков препинания и оставляю только русские

word_counts = Counter(filtered_words)  #считаю частоту каждого слова

total_words = len(filtered_words)  #запоминаю общее количество слов

for word, count in word_counts.items():  #прохожу по всем словам и их частотам
    procent = (count / total_words) * 100  #считаю процент от общего числа
    new_row = table.add_row()  #добавляю новую строку в таблицу
    new_row.cells[0].text = word  #записываю слово
    new_row.cells[1].text = str(count)  #записываю количество
    new_row.cells[2].text = str(procent)  #записываю процент

doc.save('table.docx')  #сохраняю таблицу в файл
filtered_text = ''.join(filter(lambda x: 'а' <= x <= 'я', text.lower()))  #оставляю только строчные русские буквы

letter_counts = Counter(filtered_text)  #считаю частоту каждой буквы

sorted_letters = sorted(letter_counts.keys())  #сортирую буквы по алфавиту
sorted_counts = [letter_counts[letter] for letter in sorted_letters]  #выстраиваю количества в том же порядке

plt.figure(figsize=(12, 6))  #создаю график нужного размера
plt.bar(sorted_letters, sorted_counts, color='skyblue')  #рисую столбчатую гистограмму
plt.xlabel('Буквы')  #подпись оси X
plt.ylabel('Количество')  #подпись оси Y
plt.title('Количество строчных русских букв в тексте')  #заголовок графика
plt.grid(axis='y')  #включаю сетку по оси Y

plt.tight_layout()  #подгоняю отступы
plt.show()  #показываю график