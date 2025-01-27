def tricky_function(data, values=[]):
    values.append(data)
    return values


result1 = tricky_function(1)
result2 = tricky_function(2, [])
result3 = tricky_function(3)

print(result1, result2, result3)
