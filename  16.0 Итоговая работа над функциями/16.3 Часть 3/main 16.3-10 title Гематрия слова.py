list_datas = [str(input()) for i in range(int(input()))]

def gem(word):
    total = 0
    for i in word:
        total += ord(i.upper()) - ord('A')
    return total

sort_one = sorted(list_datas)
print(*sorted(sort_one, key= lambda x: gem(x)), sep='\n')