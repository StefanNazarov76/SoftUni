from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, price: float, milliliters: float, caffeine: float) -> None:
        super().__init__(name, price, milliliters)
        self.__caffeine = caffeine

    @property
    def caffeine(self) -> float:
        return self.__caffeine
