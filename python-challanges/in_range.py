def in_range(num, lower, upper):
    if num >= lower and num<= upper:
        return True
    return False

# some tests
if in_range(14, 10, 15):
    print("You did it")
else:
    print("Well...no")

if not in_range(5, 10, 15):
    print("You did it")
else:
    print("Well...no")
        