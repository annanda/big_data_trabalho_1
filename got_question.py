import csv
import matplotlib.pyplot as plt
import numpy as np


def first_book_appeared(row):
    """
    It calculates the book that the character first appeared
    :param row: one row of dataset
    :return: the number of the book that the character of this row first appeared
    """
    book_number = 0
    for i, book in enumerate(row[8:]):
        if book == '1':
            book_number = i + 1
            return book_number
    return book_number

# reading the csv file
with open('dataset/character-deaths.csv', 'r') as file:
    data = csv.reader(file, delimiter=',')

    total_deaths = 0
# starts in 1 because of error in dataset
    total_deaths_same_book_appeared = 1

    books_deaths_appeared = {}
    deaths_in_books = {}

    for i, row in enumerate(data):
        if i is not 0:
            if row[3] != '':
                total_deaths += 1
                key_deaths = int(row[3])
                if key_deaths in deaths_in_books.keys():
                    deaths_in_books[key_deaths] += 1
                else:
                    deaths_in_books[key_deaths] = 1
                if first_book_appeared(row) == int(row[3]):
                    total_deaths_same_book_appeared += 1
                    key = int(row[3])
                    if key in books_deaths_appeared.keys():
                        books_deaths_appeared[key] += 1
                    else:
                        books_deaths_appeared[key] = 1

# the main answer
percent_deaths_same_book = (total_deaths_same_book_appeared / total_deaths) * 100
print(percent_deaths_same_book)
# print("Mortes nos livros", deaths_in_books)
# print("Mortes no mesmo livro que apareceram", books_deaths_appeared)

#graph 1
# show the number of deaths of character who appeared in the same book that they died and total deaths

N = 5
total_deaths_graph = (48, 74, 97, 27, 61)

# the x locations for the groups
ind = np.arange(N)
# the width of the bars
width = 0.35

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, total_deaths_graph, width, color='red')

same_book_deaths = (48, 54, 55, 9, 26)
rects2 = ax.bar(ind+width, same_book_deaths, width, color='darksalmon')

ax.set_ylabel('Deaths')
ax.set_title('Deaths of character who appeared in the same book that they died and total deaths')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5') )

ax.legend( (rects1[0], rects2[0]), ('Total deaths', '1st appeared deaths') )

plt.show()

#graph 2
#show the percent of deaths of character who appeared in the same book that they died
objects = ('Total deaths', 'Deaths same book')
y_pos = np.arange(len(objects))
deaths = [100, percent_deaths_same_book]

plt.bar(y_pos, deaths, align='center', alpha=0.5, width=0.45, color='red')
plt.xticks(y_pos, objects)
plt.ylabel('Percent of deaths')
plt.title('Percent of characters who dead in the same book that they first appeared')

plt.show()