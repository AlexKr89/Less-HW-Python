dict = {'Verer': 0, 'Vsd': 1, 'VI': 'S001', 'VI': 'S005', 'VII': ' S005 ', ' V ': ' S005', ' VII ': ' S005 ', 'V': ' S009 ', 'IV': 'S005'}

print(dict)
my_set = set(dict.values()) 
print(my_set)

# Вариант 2
# a = {'V': "S001", 'V': "S002", 'VI': "S001", 'VI': "S005",
#      'VI': "S005", 'VII': "  S005 ", " V ": " S009 ", " VIII ": " S007 ", "IV" : "S002"}
# b = list()
# for el in a:
#     b.append(a[el])
# print(set(b))
# a = [4,3,2,6,5,9,0]
# counter = 0
# temp = a[0]
# for el in a:
#     if el > temp:
#         counter += 1
#     temp = el
# print(counter)
