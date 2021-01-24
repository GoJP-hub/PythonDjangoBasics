print("creating a set")
set1 = {1,2,3}
print(set1)
print(type(set1))
print("*************")


print("creating a blank set")
set2 = set()
print(set2)
print(type(set2))
print("*************")

print("converting list into a set")
list1 = [1,2,3]
print(list1)
set3 = set(list1)
print(set3)
print(type(set3))
print("*************")

print("converting list into a set: removes duplicates")
list2 = [9,9,1,2,9,3]
print(list2)
set4 = set(list2)
print(set4)
print(type(set4))
print("*************")

print("add and remove from set")
print(set4)
set4.add(4)
print("set4.add(4)")
print(set4)
set4.remove(2)
print("set4.remove(2)")
print(set4)
print("*************")