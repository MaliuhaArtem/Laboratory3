try:
    import random
    array = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            array[i][j] = random.randint(1, 99)
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