
array1= [41, 47]
array2 = [1681, 2209]

def comp(array1, array2):
    return any(a1 * a1 == a2 for a1 in array1 for a2 in array2)


print(comp(array1, array2))