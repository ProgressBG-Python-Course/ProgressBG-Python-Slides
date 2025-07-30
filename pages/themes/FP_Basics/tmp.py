from functools import reduce

l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = [1, 2, 3]

# res = map(lambda *t: reduce(lambda a, c: a + c, t), l1, l2, l3)
res = map
(lambda *t: print(t), l1, l2, l3)

print(list(res))
