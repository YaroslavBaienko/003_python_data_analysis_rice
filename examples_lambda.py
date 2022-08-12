import random


list1 = list(range(21))
print(list1)


def changed(lst):
    lst = lst * 2 * random.randint(10, 200)
    return lst


list2 = list(map(changed, list1))
print(list2)

list3 = list(map(lambda num: num // 2, list2))
print("list3: ", list3)

randomlist = [random.randrange(0, num + 2) for num in list3]
print("randomlist: ", randomlist)

minpairs = list(map(lambda pair1, pair2: min(pair1, pair2), randomlist, list3))
print("mininlist: ", minpairs)
