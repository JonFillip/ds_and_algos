import timeit
from timeit import Timer
import random


# Testing the performance of Python Data structures

# Lists


def test1():
    new_list = []
    for num in range(1000):
        new_list += [num]


def test2():
    new_list = []
    for num in range(1000):
        new_list.append(num)


def test3():
    new_list = [num for num in range(1000)]


def test4():
    new_list = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("Concate ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("Append ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("Comprehension ", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")

# Concat  0.077420551 milliseconds
# Append  0.05650765199999999 milliseconds
# Comprehension  0.02597596000000002 milliseconds
# list range  0.011683866000000015 milliseconds

pop_one = Timer("x.pop(1)", "from __main__ import x")
pop_end = Timer("y.pop()", "from __main__ import y")

x = list(range(100000))
print(f"Pop 1  {pop_one.timeit(number=1000)} milliseconds")  # Pop 1
# 0.024223699000000015 milliseconds

y = list(range(100000))
print(f"Pop end {pop_end.timeit(number=1000)} milliseconds")  # Pop end
# 5.377699999997709e-05 milliseconds

popzero = Timer("x.pop(0)", "from __main__ import x")

popend = Timer("y.pop()", "from __main__ import y")

print("pop(0)  pop()")
for i in range(100000, 1000001, 100000):
    x = list(range(i))
    p_zero = popzero.timeit(number=1000)

    y = list(range(i))
    p_end = popend.timeit(number=1000)

    print(f"Pop zero running time: {p_zero}")
    print(f"Pop end running time: {p_end}")

# Results pop(0)  pop()
# Pop zero running time: 0.022923625000000003
# Pop end running time: 7.919000000000675e-05
# Pop zero running time: 0.055399639
# Pop end running time: 0.00011388200000000959
# Pop zero running time: 0.11004340499999998
# Pop end running time: 6.163900000000222e-05
# Pop zero running time: 0.09451556299999997
# Pop end running time: 4.201100000000846e-05
# Pop zero running time: 0.11395027499999999
# Pop end running time: 4.208599999999674e-05
# Pop zero running time: 0.12588442
# Pop end running time: 4.297800000008234e-05
# Pop zero running time: 0.277021489
# Pop end running time: 6.007399999985452e-05
# Pop zero running time: 0.18040783000000005
# Pop end running time: 4.357899999996029e-05
# Pop zero running time: 0.23754721300000003
# Pop end running time: 4.157800000004208e-05
# Pop zero running time: 0.285519211
# Pop end running time: 5.675199999988223e-05

"""
An experiment to check the performance efficiency using the 'in' operator to
inspect if a values in a list and a dictionary.
"""
for numb in range(10000, 100001, 200000):
    in_dict = timeit.Timer("random.randrange(%d) in x" % numb,
                           "from __main__ import random, x")
    in_list = timeit.Timer("random.randrange(%d) in y" % numb,
                           "from __main__  import random, y")

    x = list(range(numb))
    list_times = in_list.timeit(number=1000)
    y = {j: None for j in range(numb)}
    dict_time = in_dict.timeit(number=1000)

    print(f"{numb}, {list_times}, {dict_time}")  # 10000, 0.04849032200000014,
    # 0.04918504399999968
