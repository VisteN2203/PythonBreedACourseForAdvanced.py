text = str(input())

print("YES" if all([any(map(lambda x: x.isdigit(), text)),
					any(map(lambda x : x.islower(), text)),
					any(map(lambda x : x.isupper(), text)),
					len(text) > 6]) else "NO")