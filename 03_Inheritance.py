import csv


class Item:
	pay_rate = 0.8  # The pay rate after 20% discount
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
		# return f"Item('{self.name}', {self.price}, {self.quantity})" will propagate "Item" to all
		# the child class. {self.__class__.__name__} allows to associate __repr__ to child class too
		return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):

	def __init__(self, name: str, price: float, quantity=0, broken=0):
		# Call super() to inherit from Father class and pass to it the values of the inputs
		# Using super() allows to not rewrite the part of code that is common
		super().__init__(
			name, price, quantity
		)

		# Run validations to the received arguments
		assert broken >= 0, f"Broken {broken} is not greater or equal to zero!"

		# Assign to self object
		self.broken = broken


# Let' suppose we want to trace the number of phones that are broken.
# A phone is an Item so it will share all properties and methodes of Item with them and then we defne the specific attribute ("broken")
# and methods

phone1 = Phone("Samsung", 500, 5, 1)
phone2 = Phone("Huawei", 500, 5, 2)
laptop = Item('Dell', 1000, 20)
print(phone1.calculate_total_price())  # inherited method from Item
print(Item.all)
print(Phone.all)
