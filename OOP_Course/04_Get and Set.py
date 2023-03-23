import csv
from item import Item, Phone

# From this point on we will import classes from the external module item

item1 = Item("MyItem", 750)

item1._name = 'OtherItem' 	# will still overwrite it if we had _name as attribute
print(item1.name)

item1.__name = 'OtherItem' 	# will not overwrite values
print(item1.name)

item1.name = 'OtherItem' 	# This will overwrite name attribute beacause of @setter.name
print(item1.name)

# Note that all the print are the functions that GET the name, while the item.name is the one SETTING