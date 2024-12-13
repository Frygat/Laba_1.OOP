# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class Shawarma:
    """Класс, описывающий шаверму.

    Attributes:
        meat_type (str): Тип мяса (например, "курица", "говядина", "индейка").
        sauce (str): Тип соуса (например, "белый", "красный", "сметанный").
        size (str): Размер шавермы (например, "маленькая", "средняя", "большая").
    """

    def __init__(self, meat_type: str, sauce: str, size: str = "средняя"):
        """Конструктор класса Shawarma.

        Args:
            meat_type: Тип мяса.
            sauce: Тип соуса.
            size: Размер шавермы (по умолчанию "средняя").

        Raises:
            ValueError: Если тип мяса или соуса некорректен.
        """
        if meat_type not in ["курица", "говядина", "индейка"]:
            raise ValueError("Некорректный тип мяса.")
        if sauce not in ["белый", "красный", "сметанный"]:
            raise ValueError("Некорректный тип соуса.")
        self.meat_type = meat_type
        self.sauce = sauce
        self.size = size

    def eat(self) -> None:
        """Метод, имитирующий поедание шавермы.

        >>> shawarma = Shawarma("курица", "белый")
        >>> shawarma.eat()
        """
        print("Ммм, вкусная шаверма!")

    def add_ingredient(self, ingredient: str) -> None:
        """Добавляет ингредиент в шаверму.

        Args:
            ingredient: Ингредиент, который нужно добавить
                       (например, "лук", "помидоры", "огурцы").

        Raises:
            ValueError: Если ингредиент некорректен.
        """
        if ingredient not in ["лук", "помидоры", "огурцы", "капуста"]:
            raise ValueError("Некорректный ингредиент.")
        print(f"Добавлен ингредиент: {ingredient}")
# TODO: описать ещё класс
class Doshirak:
    """Класс, описывающий доширак.

    Attributes:
        flavor (str): Вкус доширака (например, "говядина", "курица", "грибы").
        spiciness (int): Острота (от 1 до 5).
    """

    def __init__(self, flavor: str, spiciness: int):
        """Конструктор класса Doshirak.

        Args:
            flavor: Вкус доширака.
            spiciness: Острота (от 1 до 5).

        Raises:
            ValueError: Если острота вне допустимого диапазона.
        """
        if not 1 <= spiciness <= 5:
            raise ValueError("Острота должна быть от 1 до 5.")
        self.flavor = flavor
        self.spiciness = spiciness

    def cook(self, water_amount: float = 0.25) -> str:
        """Готовит доширак.

        Args:water_amount: Количество воды в литрах (по умолчанию 0.25).

        Returns:
            Состояние доширака после приготовления.

        >>> doshirak = Doshirak("говядина", 3)
        >>> doshirak.cook()
        'Доширак готов!'
        """
        print("Заливаем кипятком...")
        print("Ждем 3 минуты...")
        return "Доширак готов!"

# TODO: и ещё один
class Tea:
    """Класс, описывающий чай.

    Attributes:
        tea_type (str): Тип чая (например, "черный", "зеленый", "травяной").
        water_temperature (int): Температура воды в градусах Цельсия.
    """

    def __init__(self, tea_type: str, water_temperature: int):
        """Конструктор класса Tea.

        Args:
            tea_type: Тип чая.
            water_temperature: Температура воды.

        Raises:
            ValueError: Если температура воды некорректна или не является числом.
            TypeError: Если температура воды не является числом.
        """
        if not isinstance(water_temperature, (int, float)):
            raise TypeError("Температура воды должна быть числом.")
        if not 60 <= water_temperature <= 100:
            raise ValueError(
                f"Температура воды должна быть от 60 до 100 градусов, "
                f"а не {water_temperature}."
            )
        self.tea_type = tea_type
        self.water_temperature = water_temperature

    def brew(self, brewing_time: int = 5) -> str:
        """Заваривает чай.

        Args:
            brewing_time: Время заваривания в минутах (по умолчанию 5).

        Returns:
            Описание заваренного чая.

        >>> tea = Tea("черный", 95)
        >>> tea.brew()
        'Заварен черный чай за 5 минут.'
        """
        return f"Заварен {self.tea_type} чай за {brewing_time} минут."

    def add_ingredients(self, ingredients: list[str]) -> None:
        """Добавляет ингредиенты в чай.

        Args:
            ingredients: Список ингредиентов (например, ["сахар", "лимон"]).

        Raises:
            TypeError: если ingredients не является списком.
        """
        if not isinstance(ingredients, list):
            raise TypeError("Ингредиенты должны быть представлены списком строк.")
        print(f"Добавлены ингредиенты: {', '.join(ingredients)}")