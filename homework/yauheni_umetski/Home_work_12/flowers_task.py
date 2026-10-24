from typing import Literal

FlowerParam = Literal[
    "name",
    "price",
    "color",
    "length",
    "fresh_state",
    "avg_life_time",
]


class Flower:

    def __init__(self, name: str, price: float):
        self.__name = name
        self.price = price
        self.avg_life_time: float = 1
        self.length: float = 1
        self.fresh_state: bool = True
        self.color: list[str] = []

    def __repr__(self) -> str:
        return (
            f"{self.name}(price={self.price}, length={self.length}, "
            f"color={self.color}, fresh={self.fresh_state}, life={self.avg_life_time})"
        )

    @staticmethod
    def _require_positive(target: property, value: float) -> None:
        name = target.fset.__name__
        if value <= 0:
            raise ValueError(f"{name} must be positive, got {value}")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def avg_life_time(self) -> float:
        return self._avg_life_time

    @property
    def price(self) -> float:
        return self._price

    @property
    def color(self) -> list[str]:
        return list(self._color)

    @property
    def fresh_state(self) -> bool:
        return self._fresh_state

    @property
    def length(self) -> float:
        return self._length

    @avg_life_time.setter
    def avg_life_time(self, value: float) -> None:
        self._require_positive(type(self).avg_life_time, value)
        self._avg_life_time = value

    @price.setter
    def price(self, value: float) -> None:
        self._require_positive(type(self).price, value)
        self._price = value

    @color.setter
    def color(self, value: list[str]) -> None:
        self._color = list(value)

    @fresh_state.setter
    def fresh_state(self, value: bool) -> None:
        self._fresh_state = value

    @length.setter
    def length(self, value: float) -> None:
        self._require_positive(type(self).length, value)
        self._length = value


class Rose(Flower):

    def __init__(self, price: float):
        super().__init__("Rose", price)
        self.avg_life_time = 7
        self.length = 70
        self.color = ["Red", "White", "Purple"]


class Tulip(Flower):

    def __init__(self, price: float):
        super().__init__("Tulip", price)
        self.avg_life_time = 8
        self.length = 40
        self.color = ["Red", "Yellow", "Blue", "Purple"]


class Lily(Flower):

    def __init__(self, price: float):
        super().__init__("Lily", price)
        self.avg_life_time = 8
        self.length = 39
        self.color = ["Yellow", "Blue", "Purple"]


class Bouquet:

    def __init__(self, flowers: list[Flower]):
        self._flowers = list(flowers)

    def _require_not_empty(self) -> None:
        if not self._flowers:
            raise ValueError(f"Flowers must not be empty, got {len(self._flowers)}")

    def cost_of_bouquet(self) -> float:
        self._require_not_empty()
        return sum(flower.price for flower in self._flowers)

    def avg_life_time(self) -> float:
        self._require_not_empty()
        total = sum(flower.avg_life_time for flower in self._flowers)
        return total / len(self._flowers)

    def sorted_flowers(self, param: FlowerParam) -> list[Flower]:
        self._require_not_empty()
        return sorted(self._flowers, key=lambda flower: getattr(flower, param))

    def find_flowers(self, param: FlowerParam, value: str | float | bool) -> list[Flower]:
        self._require_not_empty()
        if param == "color":
            return [flower for flower in self._flowers if value in flower.color]
        return [flower for flower in self._flowers if getattr(flower, param) == value]


rose = Rose(10.0)
tulip = Tulip(5.0)
lily = Lily(4.0)
bouquet = Bouquet([rose, tulip, lily])

sorted_bouquet = bouquet.sorted_flowers("length")
life = bouquet.avg_life_time()
cost = bouquet.cost_of_bouquet()
find = bouquet.find_flowers("name", "Rose")

print(sorted_bouquet)
print(life)
print(cost)
print(find)
