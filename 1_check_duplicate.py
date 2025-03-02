list_a = [1,2,3,5,6,8,9]
list_b = [3,2,1,5,6,0]

dup = list(set(list_a)and set(list_b))
print("Duplicates:",dup)