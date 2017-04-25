array = range(1,25)

max_number = 20
for n in range(1, max_number + 1):
    for row in range(0 , 4):
        print n + max_number * row,
    print ""
