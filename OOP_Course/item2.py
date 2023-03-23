import csv


class Item:
	pay_rate = 0.8  # The pay rate after 20% discount
	all = []

	def __init__(self, name: str, price: float, quantity=0):
		# Run validations to the received arguments
		assert price >= 0, f"Price {price} is not greater than or equal to zero!"
		assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

		# Assign to self object
		# self._name = name # read only name
		self.__name = name
		self.__price = price
		self.quantity = quantity

		# Actions to execute
		Item.all.append(self)

	@property
	# Propery decorator == Read-only attribute
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		print(f"You are setting name from {self.__name} to {value}.")
		if len(value) > 10:
			raise Exception(f"Name {value} is too long, max 10 chars")
		else:
			self.__name = value

	@property
	def price(self):
		return self.__price

	def apply_discount(self):
		self.__price = self.__price * self.pay_rate

	def apply_increment(self, value):
		self.__price = self.__price*(1+value)

	def calculate_total_price(self):
		return self.__price * self.quantity

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
		return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

	# Email methods
	def __connect(self, server):	 # private
		pass

	def __body(self): 	# private
		return f"Hello Sir/Miss.\n We have {self.quantity} {self.name}, at {self.price}€."

	def __send(self): 	# private
		pass

	def send_email(self): 	# public
		self.__connect(1)
		self.__body()
		self.__send()
		return f"Email sent:\n {self.__body()}"


class Phone(Item):
	pay_rate = 0.5
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


class Keyboard(Item):
	pay_rate = 0.7
	def __init__(self, name: str, price: float, quantity=0, broken=0):
		# Call super() to inherit from Father class and pass to it the values of the inputs
		# Using super() allows to not rewrite the part of code that is common
		super().__init__(
			name, price, quantity
		)


