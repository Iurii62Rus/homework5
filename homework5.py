immutable_var = (22, 'eggs', 1, 'bread', 'In_a_refrigerator')
print(immutable_var)
try:
    immutable_var[0] = 30
except TypeError as e:
 print("Ошибка при попытке изменить кортеж:", e)
mutable_list = [1, 2, 3, 4, 5]
print("Исходный список mutable_list:", mutable_list)
mutable_list[0] = 29
mutable_list[-1] = 11
print("Измененный список mutable_list:", mutable_list)
