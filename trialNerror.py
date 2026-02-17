from msvcrt import getwch

# variable = getwch()
# print(variable)

n = 5
for lvl in range(100):
    print(lvl, n)
    # if lvl < 10:
    n += lvl
    # elif lvl < 20:
    #     n += lvl * 2
    # elif lvl < 30:
    #     n += lvl * 4
    # else:
    #     n += lvl * 10