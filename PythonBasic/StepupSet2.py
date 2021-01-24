fruit = {'apple', 'orange', 'banana'}
color = {'red', 'orange','yellow'}
print("variable: set")
print(fruit)
print(color)
print('***************')

print('積集合: A and B')
print('fruit & color')
print(fruit & color)
print('fruit.intersection(color)')
print(fruit.intersection(color))
print('***************')

print('和集合: A or B')
print('fruit | color')
print(fruit | color)
print('fruit.union(color)')
print(fruit.union(color))
print('***************')

print('差集合: A but not B')
print('fruit - color')
print(fruit - color)
print('fruit.difference(color)')
print(fruit.difference(color))
print('***************')

print('排他的論理和： Only in A or only in B')
print('fruit ^ color')
print(fruit ^ color)
print('fruit.symmetric_difference(color)')
print(fruit.symmetric_difference(color))
print('***************')