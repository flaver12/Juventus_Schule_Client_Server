def every_third_nums(start):
    if start > 100:
        return []
    list = []
    while start <= 100:
     list.append(start)
     start += 3
    return list
    
print(every_third_nums(91))
print(every_third_nums(101))
