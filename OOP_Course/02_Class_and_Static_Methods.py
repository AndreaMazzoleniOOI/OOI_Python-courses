import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        # We need to pass self to methods. But this will be used to instantiate the object itself.
        # Thus we use a class method and we pass cls
        # THIS SHOULD DO SOMETHING THAT HAS A RELATIONSHIP WITH THE CLASS, BUT IT IS GENERALLY
        # USED TO MANIPULATE DIFFERENT STRUCTURES OF DATA TO INSTANTIATE OBJECTS
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            # Instantiate objects. Data are passed as str and must be casted
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # Check if received data is integer (Exclude numbers like 10.0). Static methods don't work on the object!!!
        # It is like an isolated function specific to the object
        # THIS SHOULD DO SOMETHING THAT HAS A RELATIONSHIP WITH THE CLASS, BUT NOT SOMETHING
        # SPECIFIC PER INSTANCE
        if isinstance(num, float):
            # Check if num is an instance of the class float. .is_integer return False whenever num has a decimal digit
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(item1.calculate_total_price())
Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(5))   # Does not apply to the specific object but to the input we send
item1.is_integer(2)     # we can also call from the instance level but does not make sense so avoid it
