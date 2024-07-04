def greet(name, *args):
    str = ""
    str += f"Hello, {name}"
    for names in args:
        str += f" and {names}"
    return str + "!"

print(greet('Timur', 'Roman'))




