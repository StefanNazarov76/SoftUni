class Shop:
    def __init__(self, name: str, _type: str, capacity: int) -> None:
        self.name = name
        self.type = _type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, _type: str):
        return cls(name, _type, 10)

    def add_item(self, item_name: str) -> str:
        if item_name in self.items and self.items[item_name] >= self.capacity:
            return 'Not enough capacity in the shop'

        self.items[item_name] = self.items.get(item_name, 0) + 1
        return f'{item_name} added to the shop'

    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount

            if self.items[item_name] <= 0:
                self.items.pop(item_name)
            return f'{amount} {item_name} removed from the shop'

        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


fresh_shop = Shop('Fresh Shop', 'Fruit and Veg', 50)
small_shop = Shop.small_shop('Fashion Boutique', 'Clothes')
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item('Bananas'))
print(fresh_shop.remove_item('Tomatoes', 2))

print(small_shop.add_item('Jeans'))
print(small_shop.add_item('Jeans'))
print(small_shop.remove_item('Jeans', 2))
print(small_shop.items)
