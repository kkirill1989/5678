#Дан список повторяющихся элементов. 
#Вернуть список с дублирующимися элементами.
#В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

my_list = [1, 3, 5, 3, 5, "tru", "tru", "test", 3]
my_list_2 = []

for item in my_list:
    if item not in my_list_2:
        if my_list.count(item) > 1:
            my_list_2.append(item)
    
print(my_list_2)