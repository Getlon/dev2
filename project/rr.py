def double(list1):
    for index, value in enumerate(list1):
        list1[index] = value * 2
    return list1


print(double([1, 2, 3, 4]))

