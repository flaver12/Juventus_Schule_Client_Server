def remove_middle(list, start, end):
  return list[:start] + list[end+1:]

print(remove_middle([1,2,4,5], 1, 3))