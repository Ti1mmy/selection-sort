def swap(a, b):
    temp = my_list[a]
    my_list[a] = my_list[b]
    my_list[b] = temp

my_list = [1, 3, 5, 8, 2, 9, 7, 3, 4, 1, 6]

for i in range(len(my_list)):
    min_index = i
    for j in range(i + 1, len(my_list)):
        if my_list[min_index] > my_list[j]:
            min_index = j
    swap(i, min_index)

print(my_list)