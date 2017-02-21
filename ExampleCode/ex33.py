
def list_numbers(end_number, increment):
    """Prints the a listing of numbers"""

    i = 0
    numbers = []

    while i < end_number:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "

    for num in numbers:
        print num


list_numbers(6,1)
