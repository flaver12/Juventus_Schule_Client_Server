def world_lenght_dictonary(diconary):
    length = {}
    for i in diconary:
        length[i] = len(diconary[i])
    return length;

print(world_lenght_dictonary({"a": "hallo", "b": "test"}))