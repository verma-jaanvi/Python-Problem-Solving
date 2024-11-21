def combining_two_lists(list1, list2):
    thisdict = dict(zip(list1, list2))

    for key, value in thisdict.items():
        print(key, value)

list1 = ["23bce10010", "23bsa12121", "23bde12123"]
list2 = ["shaurya", "ayush", "prakhar"]
combining_two_lists(list1, list2)