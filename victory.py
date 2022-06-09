# Сталин 1878
# Брежнев 1906
# Хрущев 1894
# Ленин 1870
# Путин 1952

is_play = True
while is_play:

    count = 0
    answer = int(input("Когда родился Сталин?: "))
    if answer == 1878:
        count = count + 1

    answer = int(input("Когда родился Брежнев?: "))
    if answer == 1906:
        count = count + 1

    answer = int(input("Когда родился Хрущев?: "))
    if answer == 1894:
        count = count + 1

    answer = int(input("Когда родился Ленин?: "))
    if answer == 1870:
        count = count + 1

    answer = int(input("Когда родился Путин?: "))
    if answer == 1952:
        count = count + 1

    print("Правильных ответов: ", count, " , что составляет ", count / 5 * 100, " процентов.")
    print("Неправильных ответов: ", 5 - count, " , что составляет ", (5 - count) / 5 * 100, " процентов.")

    var = input("Хотите повторить?: ")
    if var == "Нет":
        is_play = False
print("До новых встреч!!!")