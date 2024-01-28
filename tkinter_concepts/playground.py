def add(*args):
    result = 0
    for item in args:
        result = result + item
    return  result


out = add(1,2,3)
print(out)