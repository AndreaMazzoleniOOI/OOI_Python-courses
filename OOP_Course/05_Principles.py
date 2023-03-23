from item2 import Item, Phone, Keyboard

"""----------------------------- INCAPSULATION --------------------------------------------------"""
# By Incapsulation we mean setting:
# - @property for getting (read-only) values of a private attribute (__atributename)
# - setting values with a method or a @attribute.setter and not directly on the attribute (e.g. item.__price = 20)
item1 = Item("MyItem", 200, 2)
print(item1.price)

item1.apply_increment(0.2)
print(item1.price)

item1.__price = 2	 # Does not modify price
print(item1.price)

"""----------------------------- ABSTRACTION ----------------------------------------------------"""
# Abstract methods should be visible to user at some level only. For example to send an email we need
# to connect to server, create the body and then send it.
# Connecting and creating body can be methods that can be execute inside the send_email() method only,
# without cll them at the main level, which can complicate the code to much.
# This is done by adding a __ before this methods, which allows to call from the class method only.

item1.send_email()
print(item1.send_email())
# item1.__send(1) 	# Will give error

"""----------------------------- INHERITANCE ----------------------------------------------------"""
# Allows to reuse code without rewrtiting all the common methods by using the super() method

phone = Phone("Samsung", 500, 5)
phone.send_email()
print(phone.send_email())

"""----------------------------- POLYMORPHISM ----------------------------------------------------"""
name = "Jim"
list = ["some", "elem"]
print(len(name))
print(len(list))

# len knows how to deal with different objects (str and list above)

# Inherited methods can work all together

keyboard1 = Keyboard("Logitech", 200, 2)
print(f'Keyboard {keyboard1.price}€, phone {phone.price}€, Item {item1.price}€')

keyboard1.apply_discount()
phone.apply_discount()
item1.apply_discount()

print(f'Keyboard {keyboard1.price}€, phone {phone.price}€, Item {item1.price}€')
