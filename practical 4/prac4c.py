def Cloning(li1):
    li_copy = li1[:]
    return li_copy

li1 = [2, 5, 6, 3, 15, 10]
li2 = Cloning(li1)
print("Original list:", li1)
print("After Cloning:", li2)