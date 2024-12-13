from task_1 import Shawarma, Doshirak, Tea  # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
     # TODO: вызвать метод с некорректными аргументами(b)
     try:
         shawarma = Shawarma("курица", "белый")
         shawarma.add_ingredient(123)  # Некорректный тип аргумента
     except TypeError as e:
         print(f"Ошибка в Shawarma: {e}")
     except ValueError as e:
         print(f"Ошибка в Shawarma: {e}")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
     doshirak = Doshirak("говядина", 3)
     doshirak.cook(water_amount="много")  # Некорректный тип аргумента
    except TypeError as e:
        print(f"Ошибка в Doshirak: {e}")
    except ValueError as e:
        print(f"Ошибка в Doshirak: {e}")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
     tea = Tea("зеленый", 80)
     tea.brew(brewing_time=-5)  # отрицательное время заваривания
    except ValueError as e:
        print(f"Ошибка в Tea: {e}")
    except TypeError as e:
        print(f"Ошибка в Tea: {e}")
    except TypeError:
        print('Ошибка: неправильные данные')
