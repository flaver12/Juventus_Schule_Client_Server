def unqiue_values(dictionary):
    values = {}
    for i in dictionary:
        if not dictionary[i] in values.values():
            values[i] = dictionary[i]
    return values
    
print(unqiue_values({"a": 5, "b": 5, "c": 2}))
print(unqiue_values({"a": 5, "b": 5, "c": '', 'd': 4, 'f': 6}))