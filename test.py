from collections import OrderedDict

original_list = [1, 2, 3, 2, 4, 5, 1, 6]

# Использовать OrderedDict для создания уникального списка с сохранением порядка
unique_list_ordered = list(OrderedDict.fromkeys(original_list))

print(unique_list_ordered)