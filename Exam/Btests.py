from partB import Restaurant

res = Restaurant([3, 4, 4])
print(res.status())
res.print_restaurant()

print("---")

res.group_seating(("a", 2))
print(res.status())
res.print_restaurant()

print("---")

res.group_seating(("b", 2))
print(res.status())
res.print_restaurant()

print("---")

res.group_seating(("C", 8))
print(res.status())
res.print_restaurant()

print("---")

res.group_seating(("C", 5))
print(res.status())
res.print_restaurant()

print("---")

res.group_seating(("C", 4))
print(res.status())
res.print_restaurant()

print("---")

res.group_removal("b")
print(res.status())
res.print_restaurant()

print("---")

res.group_removal("C")
print(res.status())
res.print_restaurant()

print("---")

res.reset()
print(res.status())
res.print_restaurant()

rest = Restaurant([3, 2])
rest.group_seating(("GROUP1", 2))
print(rest.status()) # 2
rest.group_seating(("GROUP2", 1))
print(rest.status()) # 3
rest.group_removal("GROUP1")
print(rest.status()) # 1
rest.reset()
print(rest.status()) # 0
