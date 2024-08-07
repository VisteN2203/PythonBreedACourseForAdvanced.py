with open('../Files/lines (1).txt', 'r', encoding='utf-8') as file:
    length = len(max(file, key=len).strip())
    file.seek(0)
    print(*list(map(lambda x: x.strip(), list(filter(lambda x: x if len(x) == length + 1 else None, file)))), sep='\n')