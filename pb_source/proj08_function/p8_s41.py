def add(a, b):
    return a + b

data = (10, 20)    # tuple
#print(add(data))
print(add(*data))  # unpacking


def introduce(name, greeting):
    return "{name}님, {greeting}".format(
        name=name,
        greeting=greeting,
    )
introduce_dict = {
    "name" : "김진수",
    "greeting" : "안녕하세요",
}
print(introduce(**introduce_dict))
