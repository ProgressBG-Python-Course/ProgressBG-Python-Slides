# Кода по-долу е едно възможно решение за следната задача, но в него
# има бъг (изхода е различен от този в заданието).
# Опитайте се да разберете на какво се дължи и да го фикснете

# Напишете функция, която намира всички последователности от поне два еднакви
# елемента в списък и ги показва. Редът на показването няма значение.

# Пример:
#     вход: numbers=[2, 1, 1, 2, 3, 3, 2, 2, 2, 1],
#     изход:
#           [1,1]
#           [3,3]
#           [2,2,2]

#     вход: numbers=[4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4],
#     изход:
#          [4, 4]
#          [2, 2, 2]
#          [3, 3]
#          [4, 4, 4]


def find_similar(list_of_numbers):
    similar_lists = []

    for idx in range(1, len(list_of_numbers) - 1):
        sublist = []
        if list_of_numbers[idx] == list_of_numbers[idx + 1]:
            sublist.append(list_of_numbers[idx])
            sublist.append(list_of_numbers[idx + 1])
            count = 2
            while (idx + count) < len(list_of_numbers):
                if list_of_numbers[idx] == list_of_numbers[idx + count]:
                    sublist.append(list_of_numbers[idx + count])
                    count += 1
                else:
                    break
            similar_lists.append(sublist)
    return similar_lists


input_lists = [[2, 1, 1, 2, 3, 3, 2, 2, 2, 1], [4, 4, 2, 2, 2, 3, 3, 1, 4, 4, 4]]

for l in input_lists:
    print("Output: ")
    print(find_similar(l))
