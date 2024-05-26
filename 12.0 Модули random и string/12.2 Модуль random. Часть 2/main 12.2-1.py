import random


def generate_ip():
    list_num = list(range(1, 256))
    ip = ""
    for _ in range(4):
        ip += str(random.choice(list_num)) + "."

    return ip.rstrip(".")

print(generate_ip())
