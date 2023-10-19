try:
    import random
    rows = int(input('Введіть ціле число рядків масиву'))
    columns = int(input('Введіть ціле число колонок масиву'))
    array = [[random.randint(1, 99) for _ in range(columns)] for _ in range(rows)]
    print("Початковий масив:")
    for row in array:
        for num in row:
            print(f"{-num:-^4}", end=' ')
        print()
    x = int(input("Введіть ціле число: "))         
    print(f"Масив зі зміненими символами для чисел більших за {x}:")
    for row in array:
        for num in row:
            if num > x:
                print(f"*{num}*".center(7), end=' ')
            else:
                print(f"-{num}-".center(7), end=' ')
        print() 
except ValueError:
    print("Помилковий тип даних. Для подальшоъ роботи перезапустіть програму")