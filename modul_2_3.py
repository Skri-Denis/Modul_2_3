my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
counter = 0
while len (my_list) > counter : # цикл счетчик по индексам
    if my_list[counter] < 0: # если отрицательное - стоп цикл
        break
    else:
        if my_list[counter] >= 0 and my_list[counter] != 0 : # если положительное и не 0, то печатаем и обновляем счетчик
            print(my_list[counter])
            counter = counter + 1
        else:
            counter = counter + 1 # иначе - обновляем счетчик